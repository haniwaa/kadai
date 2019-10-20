import numpy as np
import matplotlib.pyplot as plt

# ここにグラフを描画する処理を記載する

x = [10, 20, 30, 40, 50, 60]
y = [30, 35, 45, 12, 10, 5]

plt.plot(x, y, marker="v", color = "blue", linestyle = ":")

plt.plot(x, y)
plt.show()

plt.savefig("hoge.png") # この行を追記

'''
import matplotlib.pyplot as plt

x = [100, 200, 300, 400, 500, 600]
y1 = [10, 20, 30, 50, 80, 130]
y2 = [10, 15, 30, 45, 60, 75]

plt.plot(x, y1, marker="o", color = "red", linestyle = "--")
plt.plot(x, y2, marker="v", color = "blue", linestyle = ":")
plt.show()

plt.savefig("hoge.png") # この行を追記
'''

'''
import matplotlib.pyplot as plt

x = [100, 200, 300, 400, 500, 600]
y1 = [10, 20, 30, 50, 80, 130]
y2 = [10, 15, 30, 45, 60, 75]

fig = plt.figure()

# 1行2列に分割した中の1(左側)
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x, y1, marker="o", color = "red", linestyle = "--")

# 1行2列に分割した中の2(右側)
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x, y2, marker="v", color = "blue", linestyle = ":")

plt.show()

plt.savefig("hoge.png") # この行を追記
'''

#techacademy --- https://techacademy.jp/magazine/19316
