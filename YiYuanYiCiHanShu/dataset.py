import numpy as np


def getBeans(count=10):
    """
    生成随机豆豆
    """
    xs = np.random.rand(count)
    xs = np.sort(xs)
    ys = [1.2 * x + np.random.rand() / 10 for x in xs]
    return xs, ys
