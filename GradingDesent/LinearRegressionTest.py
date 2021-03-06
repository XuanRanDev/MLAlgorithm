import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

lr = 0.00001
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


def gradient(data, theta, y):
    """
    计算梯度
    :param data:
    :param theta:
    :param y:
    :return:
    """
    grad = np.empty(len(theta))
    grad[0] = np.sum(data.dot(theta) - y)
    for i in range(1, len((theta))):
        grad[i] = (data.dot(theta) - y).dot(data[:, i])
    return grad


def gradient_decent(data, theta, y, eta):
    while True:
        last_theta = theta
        grad = gradient(data, theta, y)
        theta = theta - eta * grad
        print(theta)
        """
        为什么需要小于等于1E-15?
        因为计算机精度的问题其结果只能小于一个很小的数字
        否则，这个循环会不断执行
        """
        if abs(cost_function(data, last_theta, y)) - cost_function(data, theta, y) <= 1E-15:
            break

    return theta


if __name__ == '__main__':
    res = gradient_decent(data, theta, y, lr)
    X = np.arange(3, 25)
    Y = res[0] + res[1] * X
    plt.plot(X, Y, color='r')
    plt.show()

