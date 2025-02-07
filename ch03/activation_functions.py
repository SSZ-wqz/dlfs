import numpy as np
import matplotlib.pyplot as plt

# np数组实现
def step_function(x):
  return np.array(x > 0, dtype=int)

def sigmoid_function(x):
  return 1 / (1 + np.exp(-x))

def main():
  x = np.arange(-5.0, 5.0, 0.1)
  y = step_function(x)
  z = sigmoid_function(x)
  plt.plot(x, y, linestyle="--", label="step_function")
  plt.plot(x, z, linestyle="-", label="sigmoid_function")
  plt.title("activation functions")
  plt.show()

if __name__ == "__main__":
  main()