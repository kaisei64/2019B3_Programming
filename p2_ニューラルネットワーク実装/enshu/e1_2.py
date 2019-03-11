from e1_1 import Perceptron

if __name__ == "__main__":
    AND = Perceptron(1.1, 2.1, 2.2)

if __name__ == "__main__":
    NAND = Perceptron(-1.1, -2.1, -2.2)

if __name__ == "__main__":
    OR = Perceptron(0.5, 0.2, 0.1)

x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]

for x1, x2 in zip(x1_list,x2_list):
    print("AND({0}, {1}) = {2}  ".format(x1, x2, AND.Forward(x1, x2)), end="")
    print("NAND({0}, {1}) = {2}  ".format(x1, x2, NAND.Forward(x1, x2)), end="")
    print("OR({0}, {1}) = {2}  ".format(x1, x2, OR.Forward(x1, x2)))