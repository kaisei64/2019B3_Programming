import numpy as np
from e2_2 import Relu

class SingleLayer:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def Forward(self, x):
        y = np.dot(x, self.w) + self.b
        return Relu(y)

def main():
    x = np.array([1.0, 0.5])
    w = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    b = np.array([0.1, 0.2, 0.3])

    layer = SingleLayer(w, b)
    print(layer.Forward(x))

if __name__ == "__main__":
    main()