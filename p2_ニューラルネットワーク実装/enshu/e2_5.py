import numpy as np
from e2_2 import Relu

class MLP_3Layer:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def Forward(self, x):
        y = np.dot(x, self.w) + self.b
        return Relu(y)

    def Forward2(self, x):
        y = np.dot(x, self.w) + self.b
        return Softmax(y)

def Softmax(x):
    exp_x = np.exp(x)
    y = exp_x / np.sum(np.exp(x), axis=1, keepdims=True)
    return y

def main():
    x = np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])
    W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    b1 = np.array([0.1, 0.2, 0.3])
    W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    b2 = np.array([0.1, 0.2])
    W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
    b3 = np.array([0.1, 0.2])

    layer1 = MLP_3Layer(W1, b1)
    layer2 = MLP_3Layer(W2, b2)
    layer3 = MLP_3Layer(W3, b3)
    x1 = layer1.Forward(x)
    x2 = layer2.Forward(x1)
    x3 = layer3.Forward2(x2)
    #print(layer1.Forward(x))
    #print(layer2.Forward(x1))
    print(x3)


if __name__ == "__main__":
    main()