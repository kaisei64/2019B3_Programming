import numpy as np
import math

e = math.e

def Relu(x):
    return np.maximum(0, x)

def main():
    x = np.array([-1.0, 0.0, 0.5, 2.0])

    print(Relu(x))

if __name__ == "__main__":
    main()