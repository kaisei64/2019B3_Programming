class Multiply():
    def __init__(self):
        """ 逆伝播計算に必要な変数：forwardの入力値 """
        self.x = None
        self.y = None
    def forward(self, x, y):
        """ 順伝播計算：z = x * y """
        self.x = x
        self.y = y
        z = x * y
        return z
    def backprop(self, dz):
        """ 逆伝播計算: dz/dx = y, dz/dy = x """
        dx = dz * self.y
        dy = dz * self.x
        return dx, dy

class Add():
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self, x, y):
        self.x = x
        self.y = y
        z = x + y
        return z
    def backprop(self, dz):
        dx = dz
        dy = dz
        return dx, dy

def main():
    a = 2
    b = 3
    c = 4

    add = Add()
    mul = Multiply()

    x1 = add.forward(a, b)
    x2 = mul.forward(x1, c)
    print("順伝播出力: {0}".format(x2))

    dx1, dc = mul.backprop(1)
    da, db = add.backprop(dx1)
    print("逆伝播出力 da: {0}, db: {1}, dc: {2}".format(da, db, dc))

if __name__ == "__main__":
    main()