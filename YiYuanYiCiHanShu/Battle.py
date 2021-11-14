import dataset
from matplotlib import pyplot as plt

# 生成豆豆 xs为豆豆大小 ys为豆豆的毒性
xs, ys = dataset.getBeans(100)
# 配置图像
plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Bean Toxicity")

alpha = 0.01  # 设置防止大幅震荡的学习率
w = 0.5

for k in range(100):

    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        y_pre = w * x
        e = y - y_pre
        w = w + alpha * e * x  # 加入学习率减少震荡

y_pre = w * xs
plt.plot(xs, y_pre)
plt.scatter(xs, ys)
plt.show()

