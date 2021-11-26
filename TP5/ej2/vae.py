from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import tensorflow as tf

from keras.layers import Input, Dense, Lambda
from keras.models import Model
from keras import backend as K
from keras import metrics

from tensorflow.python.framework.ops import disable_eager_execution

disable_eager_execution()

import tensorflow_datasets as tfds

# 2. Download and Parse Dataset

dataset_name: str = 'fashion_mnist'
ds_train = tfds.load(dataset_name, split='train', as_supervised=True)

x_train: [] = []
y_train: [] = []
for image, label in tfds.as_numpy(ds_train):
    x_train.append(image)
    y_train.append(label)

x_test: [] = []
y_test: [] = []
try:
    ds_test = tfds.load(dataset_name, split='test', as_supervised=True)
    for image, label in tfds.as_numpy(ds_test):
        x_test.append(image)
        y_test.append(label)
except:
    x_test = x_train
    y_test = y_train

x_train = np.asarray(x_train)
data_shape = x_train.shape
x_train = x_train.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))

x_test = np.asarray(x_test)
x_test = x_test.astype('float32') / 255.
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

# 3. Setting up Parameters

print(x_train.shape)
batch_size = 100
original_dim = x_train.shape[1]
latent_dim = 2
intermediate_dim = 256
epochs = 100
epsilon_std = 1.0


def sampling(args: tuple):
    # we grab the variables from the tuple
    z_mean, z_log_var = args
    print(z_mean)
    print(z_log_var)
    epsilon = K.random_normal(shape=(K.shape(z_mean)[0], latent_dim), mean=0.,
                              stddev=epsilon_std)
    return z_mean + K.exp(z_log_var / 2) * epsilon  # h(z)


# 4. Encoder

# input to our encoder
x = Input(shape=(original_dim,), name="input")
# intermediate layer
h = Dense(intermediate_dim, activation='relu', name="encoding")(x)
# defining the mean of the latent space
z_mean = Dense(latent_dim, name="mean")(h)
# defining the log variance of the latent space
z_log_var = Dense(latent_dim, name="log-variance", kernel_initializer=tf.initializers.RandomNormal(stddev=0.01),
                  bias_initializer=tf.initializers.Zeros())(h)
# note that "output_shape" isn't necessary with the TensorFlow backend
z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])
# defining the encoder as a keras model
encoder = Model(x, [z_mean, z_log_var, z], name="encoder")

# print out summary of what we just did
# encoder.summary()


# 5. Decoder

# Input to the decoder
input_decoder = Input(shape=(latent_dim,), name="decoder_input")
# taking the latent space to intermediate dimension
decoder_h = Dense(intermediate_dim, activation='relu', name="decoder_h")(input_decoder)
# getting the mean from the original dimension
x_decoded = Dense(original_dim, activation='sigmoid', name="flat_decoded")(decoder_h)
# defining the decoder as a keras model
decoder = Model(input_decoder, x_decoded, name="decoder")

# print ummary
# decoder.summary()


# 6. Full AutoEncoder

# grab the output. Recall, that we need to grab the 3rd element our sampling z
output_combined = decoder(encoder(x)[2])
# link the input and the overall output
vae = Model(x, output_combined)


# print out what the overall model looks like
# vae.summary()


# 7. Loss Function (optimization)

def vae_loss(x: tf.Tensor, x_decoded_mean: tf.Tensor):
    # Aca se computa la cross entropy entre los "labels" x que son los valores 0/1 de los pixeles, y lo que salió al final del Decoder.
    xent_loss: float = original_dim * metrics.binary_crossentropy(x, x_decoded_mean)  # x-^X
    kl_loss = - 0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
    vae_loss = K.mean(xent_loss + kl_loss)
    return vae_loss


vae.compile(loss=vae_loss, experimental_run_tf_function=False)


# 8. Train AutoEncoder

vae.fit(x_train, x_train,
        shuffle=True,
        epochs=epochs,
        batch_size=batch_size)

# 9. Plot Latent Space

x_test_encoded = encoder.predict(x_test, batch_size=batch_size)[0]
plt.figure(figsize=(6, 6))
plt.scatter(x_test_encoded[:, 0], x_test_encoded[:, 1], c=y_test, cmap='viridis')
plt.colorbar()
plt.show()

# 10. Generate

n: int = 10
(_, h_size, w_size, c_size) = data_shape

grid_x = norm.ppf(np.linspace(0.05, 0.95, n))
grid_y = norm.ppf(np.linspace(0.05, 0.95, n))

plt.figure(figsize=(10, 10))

if c_size == 1:
    figure = np.zeros((h_size * n, w_size * n))
    for i, yi in enumerate(grid_x):
        for j, xi in enumerate(grid_y):
            z_sample = np.array([[xi, yi]])
            x_decoded = decoder.predict(z_sample)
            digit = x_decoded[0].reshape(h_size, w_size)
            figure[i * h_size: (i + 1) * h_size,
            j * w_size: (j + 1) * w_size] = digit

    plt.imshow(figure, cmap='gray')

elif c_size == 3:
    figure = np.zeros((h_size * n, w_size * n, c_size))
    for i, yi in enumerate(grid_x):
        for j, xi in enumerate(grid_y):
            z_sample = np.array([[xi, yi]])
            x_decoded = decoder.predict(z_sample)
            digit = x_decoded[0].reshape(h_size, w_size, c_size)
            figure[i * h_size: (i + 1) * h_size,
            j * w_size: (j + 1) * w_size,
            :] = digit

    plt.imshow(figure)

plt.show()

print(grid_x)

print(z_sample)