import matplotlib.pyplot as plt
import numpy as np

plt.ion()
for i in range(1907):
    # y = np.random.random([10,1])
    plt.scatter(sbus[5]['lat'].values[i*5], sbus[5]['lon'].values[i*5])
    print(sbus[5]['lat'].values[i], sbus[5]['lon'].values[i])
    plt.draw()
    plt.pause(0.000001)
    plt.clf()