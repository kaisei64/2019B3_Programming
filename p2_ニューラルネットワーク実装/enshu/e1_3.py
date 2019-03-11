from e1_1 import Perceptron

if __name__ == "__main__":
    AND = Perceptron(1.1, 2.1, 2.2)

if __name__ == "__main__":
    NAND = Perceptron(-1.1, -2.1, -2.2)

if __name__ == "__main__":
    OR = Perceptron(0.5, 0.2, 0.1)

def XOR(x1, x2):
    s1 = Perceptron(-1.1, -2.1, -2.2)
    s2 = Perceptron(0.5, 0.2, 0.1)
    s3 = Perceptron(1.1, 2.1, 2.2)
    t1 = s1.Forward(x1, x2)
    t2 = s2.Forward(x1, x2)
    y = s3.Forward(t1, t2)
    return y

def main():
    x1_list = [1, 1, 0, 0]
    x2_list = [1, 0, 1, 0]

    for x1, x2 in zip(x1_list,x2_list):
        print("XOR({0}, {1}) = {2}  ".format(x1, x2, XOR(x1, x2)))

if __name__ == "__main__":
    main()