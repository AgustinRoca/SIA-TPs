import matplotlib.pyplot as plt

f = open("./results/ej1/error.txt")
errors = f.readlines()
errors = [float(x) for x in errors]

plt.plot(errors)
plt.show()