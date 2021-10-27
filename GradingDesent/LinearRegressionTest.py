import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = "data.txt"
data = pd.read_csv(path, header=None)
plt.scatter(data[:][0], data[:][1], marker='+')

data = np.array(data)
m = data.shape[0]
theta = np.array([0, 0])
data = np.hstack([np.ones([m, 1]), data])
y = data[:, 2]
data = data[:, :2]


def cost_function(data, theta, y):
    cost = np.sum((data.dot(theta) - y) ** 2)
    return cost / (m * 2)


