import dataset
from matplotlib import pyplot as plt

# 生成豆豆 xs为豆豆大小 ys为豆豆的毒性
xs, ys = dataset.getBeans(100)

# 配置图像
plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Bean Toxicity")

w = 0.01
y_pre = w * xs

plt.plot(xs, y_pre)


plt.scatter(xs, ys)
plt.show()