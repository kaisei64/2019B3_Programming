import numpy as np

class Sigmoid:
    def __init__(self):
        self.out = None
    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out
    def backprop(self, dout):
        return dout * (1.0 - self.out) * self.out

def main():
    x = np.array([-0.5, 0.0, 1.0, 2.0])

    sig = Sigmoid()

    x1 = sig.forward(x)
    print("順伝播出力: {0}".format(x1))

    dx1 = sig.backprop(1.)
    print("逆伝播出力: {0}".format(dx1))

if __name__ == "__main__":
    main()