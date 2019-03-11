from e3_2 import *
from e3_4 import *
from e3_5 import *

from collections import OrderedDict


class NeuralNetwork:
    def __init__(self):
        self.pm = {'W1': np.random.normal(0, 0.1, (784, 500)),
                   'b1': 0.01,
                   'W2': np.random.normal(0, 0.1, (500, 10)),
                   'b2': 0.01}

        """self.layers['add'] = Add()
        self.layers['mul'] = Multiply()
        self.layers['relu'] = Relu()
        self.layers['sig'] = Sigmoid()
        self.layers['aff'] = Affine(self.pm['W1'], self.pm['b1'])"""
        self.layers = OrderedDict()
        self.layers['aff1'] = Affine(self.pm['W1'], self.pm['b1'])
        self.layers['relu'] = Relu()
        self.layers['aff2'] = Affine(self.pm['W2'], self.pm['b2'])

        self.last = SoftmaxCrossEntropy()

    def forward(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
        return x

    def loss(self, x, t):
        y = self.forward(x)
        return self.last.forward(y, t)

    def backprop(self, x, t):
        self.loss(x, t)

        dout = 1
        dout = self.last.backprop(dout)
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backprop(dout)

        grads = {'W1': self.layers['aff1'].dW,
                 'b1': self.layers['aff1'].db,
                 'W2': self.layers['aff2'].dW,
                 'b2': self.layers['aff2'].db}

        return grads

    def sgd(self, x, t, learning_rate):
        grads = self.backprop(x, t)
        for key in ('W1', 'b1', 'W2', 'b2'):
            self.pm[key] -= learning_rate * grads[key]
