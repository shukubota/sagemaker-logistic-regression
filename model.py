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
  
  def input_fn(self, params):
    return [params.get('petal_length'), params.get('petal_width')]
  
  def output_fn(self, category_index):
    return ['Iris-Setosa', 'Iris-Versicolour'][category_index]