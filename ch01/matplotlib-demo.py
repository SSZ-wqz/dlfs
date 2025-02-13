import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0, 6, 0.1)  # 以0.1为单位，生成0到6的数据 [0.  0.1 0.2 0.3 0.4 0.5 0.6 ... 5.5 5.6 5.7 5.8 5.9]
y = np.sin(x)

# 绘制图形
plt.plot(x, y)
plt.show()