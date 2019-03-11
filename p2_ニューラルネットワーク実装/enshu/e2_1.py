import numpy as np
import math


def Sigmoid(x):
    return 1 / (1 + e**-x)

x = np.array([-1.0, 0.0, 0.5, 2.0])
e = math.e

print(Sigmoid(x))