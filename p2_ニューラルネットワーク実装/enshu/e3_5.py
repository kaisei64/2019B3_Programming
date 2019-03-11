import numpy as np


class SoftmaxCrossEntropy:
    def __init__(self):
        self.l = None
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.t = t
        self.y = Softmax(x)
        self.l = cross_entropy(self.y, self.t)
        return self.l

    def backprop(self):
        dx = (self.y - self.t)
        return dx


def Softmax(x):
    exp_x = np.exp(x)
    y = exp_x / np.sum(np.exp(x), axis=1, keepdims=True)
    return y


'''def cross_entropy_error(y, t):
    if y.ndim == 1: # データは横に並べる
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 教師データがone-hot-vectorの場合、正解ラベルのインデックスに変換
    if t.size == y.size:
        t = t.argmax(axis=1)
    batch_size = y.shape[0] # 縦方向の数＝バッチ処理するデータの数
    return -np.sum(np.log(y[np.arange(batch_size), t])) / batch_size'''


def cross_entropy(y, t):
    one_sample_loss = np.sum(-t * np.log(y), axis=1)
    return np.average(one_sample_loss)


if __name__ == "__main__":
    x = np.array([[1.0, 0.5], [-0.4, 0.1]])
    t = np.array([[1.0, 0.0], [0.0, 1.0]])

    soft = SoftmaxCrossEntropy()

    x1 = soft.forward(x, t)
    print("順伝播出力: \n{0}".format(x1))

    dx = soft.backprop()
    print("逆伝播出力: \n{0}".format(dx))
