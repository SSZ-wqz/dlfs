import numpy as np    # 将 numpy 作为 np 导入

# 1.5.2 生成 NumPy 数组
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(x)
print(type(x))


# 1.5.3 NumPy 的算术运算
y = np.array([1,2,3,4])
z = np.array([2,4,6,8])

# 对应元素的加法
print("y + z: ", y + z)
print("y - z: ", y - z)
print("y * z: ", y * z)
print("y / z: ", y / z)


# 1.5.4 NumPy 的 N 维数组
A = np.array([ [1,2], [3,4] ])
print("A => \n", A)
# 对应元素的乘法
A *= 10
print("A*10 => \n", A)


# 1.5.5 广播
A = np.array([[10,20],[30,40]])
B = np.array([2,4])
print("A * B => \n", A * B)   # should be [ [20, 80], [60, 160] ]


# 1.5.6 访问元素
X = np.array([[51, 55], [14, 19], [0, 4]])
print("X", X)
# 访问第一行
print("X的第一行 ", X[0])
# 第一行的第二列， 应该是14
print("第一行的第二列， 应该是14 ", X[0][1])

for row in X:
  print(row)
  
print(X.flatten())

print(X > 15)