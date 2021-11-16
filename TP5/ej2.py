import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from keras.layers import Input, Dense, Lambda
from keras.models import Model
from keras import backend as K
from keras import metrics
import tensorflow_datasets as tfds


def train_tf(dataset_name):
    x = []
    y = []
    dataset = tfds.load(dataset_name, split='test', as_supervised=True)
    for image, label in tfds.as_numpy(dataset):
        x.append(image)
        y.append(label)

    return dataset, x, y


def train_and_test_tf(dataset_name):
    training_dataset, x_train, y_train = train_tf(dataset_name)
    testing_dataset, x_test, y_test = train_tf(dataset_name)

    x_train = np.asarray(x_train)
    data_shape = x_train.shape
    x_train = x_train.astype('float32') / 255.
    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))

    x_test = np.asarray(x_test)
    x_test = x_test.astype('float32') / 255.
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

    return data_shape, (x_train, y_train), (x_test, y_test)


def create_encoder(input_shape, hidden_shape, latent_shape, epsilon_std):
    def sampling(args):
        epsilon = K.random_normal(shape=(K.shape(z_mean)[0], latent_shape), mean=0., stddev=epsilon_std)
        return args[0] + K.exp(args[1] / 2) * epsilon

    x = Input(shape=(input_shape,), name="input")
    h = Dense(hidden_shape, activation='relu', name="encoding")(x)
    z_mean = Dense(latent_shape, name="mean")(h)
    z_log_var = Dense(latent_shape, name="log-variance")(h)
    z = Lambda(sampling, output_shape=(hidden_shape,))([z_mean, z_log_var])
    encoder = Model(x, [z_mean, z_log_var, z], name="encoder")

    return encoder, x, z_log_var, z_mean


def create_decoder(input_shape, hidden_shape, latent_shape):
    # Input to the decoder
    input_decoder = Input(shape=(latent_shape,), name="decoder_input")
    # taking the latent space to intermediate dimension
    decoder_h = Dense(hidden_shape, activation='relu', name="decoder_h")(input_decoder)
    # getting the mean from the original dimension
    x_decoded = Dense(input_shape, activation='sigmoid', name="flat_decoded")(decoder_h)
    # defining the decoder as a keras model
    decoder = Model(input_decoder, x_decoded, name="decoder")

    return decoder


def create_ae(encoder, decoder, x):
    output_combined = decoder(encoder(x)[2])
    return Model(x, output_combined)


def train(variable_ae, x_train, epochs, batch):
    variable_ae.fit(
        x_train,
        x_train,
        shuffle=True,
        epochs=epochs,
        batch_size=batch
    )


def plot_latent(encoder, test_results, batch):
    x_test_encoded = encoder.predict(test_results[0], batch_size=batch)[0]
    plt.figure(figsize=(6, 6))
    plt.scatter(x_test_encoded[:, 0], x_test_encoded[:, 1], c=test_results[1], cmap='viridis')
    plt.colorbar()
    plt.show()


def generate(decoder, data_shape):
    n = 3
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
                figure[i * h_size: (i + 1) * h_size, j * w_size: (j + 1) * w_size] = digit

        plt.imshow(figure, cmap='gray')
    elif c_size == 3:
        figure = np.zeros((h_size * n, w_size * n, c_size))
        for i, yi in enumerate(grid_x):
            for j, xi in enumerate(grid_y):
                z_sample = np.array([[xi, yi]])
                x_decoded = decoder.predict(z_sample)
                digit = x_decoded[0].reshape(h_size, w_size, c_size)
                figure[i * h_size: (i + 1) * h_size, j * w_size: (j + 1) * w_size, :] = digit

        plt.imshow(figure)

    plt.show()


def main():
    data_shape, train_results, test_results = train_and_test_tf('quickdraw_bitmap')

    input_shape = train_results[0].shape[1]
    latent_shape = 2
    hidden_shape = 256

    batch = 100
    epochs = 50
    epsilon_std = 1.0

    encoder, x, z_log_var, z_mean = create_encoder(input_shape, hidden_shape, latent_shape, epsilon_std)
    decoder = create_decoder(input_shape, hidden_shape, latent_shape)
    variable_ae = create_ae(encoder, decoder, x)

    def variable_ae_loss(x, x_decoded_mean):
        xent_loss = input_shape * metrics.binary_crossentropy(x, x_decoded_mean)  # x-^X
        kl_loss = - 0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
        vae_loss = K.mean(xent_loss + kl_loss)
        return vae_loss

    variable_ae.compile(loss=variable_ae_loss, experimental_run_tf_function=False)

    train(variable_ae, x[0], epochs, batch)
    plot_latent(encoder, test_results, batch)

    generate(decoder, data_shape)


if __name__ == '__main__':
    main()
