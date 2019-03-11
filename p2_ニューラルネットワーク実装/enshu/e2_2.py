import numpy as np
import math


def Relu(x):
    return np.maximum(0, x)

x = np.array([-1.0, 0.0, 0.5, 2.0])
e = math.e

print(Relu(x))