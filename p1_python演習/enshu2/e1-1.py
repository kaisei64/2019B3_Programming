class Perceptron:
    def __init__(self, w1, w2, theta):
        self.w1 = w1
        self.w2 = w2
        self.theta = theta

    def Forward(self, x1, x2):
        y = self.w1 * x1 + self.w2 * x2
        if y >= self.theta:
            return 1
        elif y < self.theta:
            return 0

if __name__ == "__main__":
    AND = Perceptron(1.1, 2.1, 2.2)

if __name__ == "__main__":
    NAND = Perceptron(-1.1, -2.1, -2.2)

if __name__ == "__main__":
    OR = Perceptron(0.5, 0.2, 0)

x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]

for i,j in x1_list,x2_list:
    print("AND(%d, %d) = %d",%(x1_list[i], x2_list[j], AND.Forward(x1_list[i], x2_list[j])), end="")
    print("NAND(%d, %d) = %d", % (x1_list[i], x2_list[j], NAND.Forward(x1_list[i], x2_list[j])), end="")
    print("OR(%d, %d) = %d", % (x1_list[i], x2_list[j], OR.Forward(x1_list[i], x2_list[j])))