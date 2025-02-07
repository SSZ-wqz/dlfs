import matplotlib.pyplot as plt
from matplotlib.image import imread

# 1.6.3 显示图像
img = imread("dataset/profile.png")
plt.imshow(img)

plt.show()