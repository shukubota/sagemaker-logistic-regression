from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

# gradient descent 最急降下法
class LogisticRegressionGD(object):
  # eta: float # 学習率
  # n_iter: int # トレーニング回数
  # random_state: int # 乱数シード(初期化用)
  # w_ # (重み行列)
  # const_ # 誤差平方和コスト関数

  def __init__(self, eta=0.05, n_iter=100, random_state=1):
    self.eta = eta
    self.n_iter = n_iter
    self.random_state = random_state
    rgen = np.random.RandomState(self.random_state)
    self.w_ = rgen.normal(loc = 0.0, scale = 0.01, size = 3)

  #z(推定値)を計算する
  def net_input(self, x):
    return np.dot(x, self.w_[1:]) + self.w_[0]

  def activation(self, z):
    # シグモイド活性化関数
    # return 1. / (1. + np.exp(-np.clip(z, -250, 250)))
    return 1. / (1. + np.exp(-z))

  def fit(self, x, y):
    # x: n * 2次元ベクトル(n個の2次元ベクトル)
    # y: n個のラベル

    rgen = np.random.RandomState(self.random_state)
    # https://numpy.org/doc/1.16/reference/generated/numpy.random.RandomState.normal.html#numpy.random.RandomState.normal
    # loc 分布の平均
    # scale 標準偏差
    # w0*x0 + w1*x1 + w2*x2
    self.w_ = rgen.normal(loc = 0.0, scale = 0.01, size = 1 + x.shape[1])
    self.cost_ = []

    for i in range(self.n_iter):
      net_input = self.net_input(x)
      # outputは\phi(z)
      output = self.activation(net_input)
      errors = y - output

      self.w_[1:] += self.eta * x.T.dot(errors)
      self.w_[0] += self.eta * errors.sum()

      cost = -y.dot(np.log(output)) - ((1- y).dot(np.log(1 - output)))
      self.cost_.append(cost)

  def predict(self, x):
    return np.where(self.net_input(x) >= 0.0, 1, 0)

if __name__ == '__main__':
  iris = datasets.load_iris()
  x = iris.data[:, [2, 3]]
  y = iris.target

  # 30%をtestにする
  x_train, x_test, y_train, y_test = train_test_split(x, y ,test_size = 0.3, random_state = 1, stratify = y)
  x_train_01_subset = x_train[(y_train == 0) | (y_train == 1)]
  y_train_01_subset = y_train[(y_train == 0) | (y_train == 1)]

  x_test_01_subset = x_train[(y_train == 0) | (y_train == 1)]
  y_test_01_subset = y_train[(y_train == 0) | (y_train == 1)]

  estimator = LogisticRegressionGD(eta = 0.05, n_iter = 1000, random_state = 1)

  output = estimator.predict(x_test_01_subset)
  print(estimator.w_)
  print(output)
  print(y_test_01_subset)

  estimator.fit(x_train_01_subset, y_train_01_subset)

  print(estimator.w_)

  # 推論
  output = estimator.predict(x_test_01_subset)

  print(output)
  print(y_test_01_subset)

  test = output[output != y_test_01_subset]
  print(len(test))

  
