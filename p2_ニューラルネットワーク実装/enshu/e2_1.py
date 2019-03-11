import numpy as np
import math

e = math.e

def Sigmoid(x):
    return 1 / (1 + e**-x)

def main():
    x = np.array([-1.0, 0.0, 0.5, 2.0])

    print(Sigmoid(x))

if __name__ == "__main__":
    main()