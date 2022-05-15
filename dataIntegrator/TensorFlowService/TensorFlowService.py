# import tensorflow as tf
# import numpy as np
# import matplotlib.pyplot as plt


class TensorFlowService:
    selfName = ""

    # def __init__(self):
    #     print("__init__")
    #
    # #@staticmethod
    # def prepareData(self):
    #     print("starting func1")
    #     np.random.seed(5)
    #
    #     xData = np.linspace(-1, 1, 100)
    #     yData = 2 * xData + 1.0 + np.random.randn(*xData.shape) * 0.4
    #
    #     print(xData)
    #     print(yData)
    #
    #     plt.scatter(xData, yData)
    #     plt.plot(xData, 2 * xData + 1.0, color='red', linewidth=3)
    #
    #     plt.show()
    #
    # #@staticmethod
    # def trainModel(self):
    #     tf.compat.v1.disable_eager_execution()  # 用tf.compat.v1.来兼容tensorflow版本1的方法。
    #     x = tf.compat.v1.placeholder("float", name="x")
    #     y = tf.compat.v1.placeholder("float", name="y")
    #
    #     # 定义模型函数
    #     def model(x, w, b):
    #         return tf.multiply(x, w) + b
    #
    #     # 构建线性函数的斜率和截距，都为变量，tf.Variable为变量声明函数
    #     w = tf.Variable(1.0, name="w0")
    #     b = tf.Variable(0.0, name="b0")
    #
    # def readData(self):
    #     my_data = np.genfromtxt('dataset.csv', delimiter=',', dtype=float)
    #     x_data = np.array(my_data[:, 0])
    #     y_data = np.array(my_data[:, 1])
    #
    #     print(x_data)
    #     print(y_data)
    #
    #     weights = tf.Variable(tf.random_uniform([1], -1, 0, 1.0))
    #     biases = tf.Variable(tf.zeros([1]))
    #
    #     y = weights*x_data + biases
    #
    #     loss = tf.reduce_mean(tf.square(y - y_data))
    #
    #     optimizer = tf.train.GradientDescentOptimizer(0.5)
    #
    #     optimizer = tf.train.GradientDescentOptimizer(0.5)
    #     train = optimizer.minimize(loss)
    #
    #     init = tf.global_variables_initializer()
    #
    #     sess = tf.Session()
    #     sess.run(init)
    #
    #     for step in range(201):
    #         sess.run(train)
    #         if step % 20 == 0:
    #             print(step, 'weight: ',sess.run(weights), ' bias: ', sess.run(biases))