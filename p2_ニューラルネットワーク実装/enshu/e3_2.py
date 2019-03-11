import numpy as np

class Relu:
    def __init__(self):
        self.mask = None
    def forward(self, x):
        self.mask = (x>0).astype(int)
        out = x.copy()
        out[self.mask] = 0
        return out
    def backprop(self, dout):
        return dout * self.mask

def main():
    x = np.array([-0.5, 0.0, 1.0, 2.0])

    relu = Relu()

    x1 = relu.forward(x)
    print("順伝播出力: {0}".format(x1))

    dx1 = relu.backprop(1.)
    print("逆伝播出力: {0}".format(dx1))

if __name__ == "__main__":
    main()