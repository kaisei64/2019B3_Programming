import numpy as np


class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out

    def backprop(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        return dx


def main():
    x = np.array([[1.0, 0.5], [-0.4, 0.1]])
    W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    b = np.array([0.1, 0.2, 0.3])

    aff = Affine(W, b)

    x1 = aff.forward(x)
    print("順伝播出力: \n{0}".format(x1))

    dx = aff.backprop(np.ones([2, 3]))
    print("逆伝播出力dx: \n{0}".format(dx))
    print("逆伝播出力dw: \n{0}".format(aff.dW))
    print("逆伝播出力db: \n{0}".format(aff.db))


if __name__ == "__main__":
    main()