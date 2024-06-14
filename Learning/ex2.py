class ExtendedStack(list):
    def sum(self):
        # операция сложения
        x1 = self.pop(-1)
        x2 = self.pop(-1)
        x3 = x1 + x2
        self.append(x3)
    def sub(self):
        # операция вычитания
        x1 = self.pop(-1)
        x2 = self.pop(-1)
        x3 = x1 - x2
        self.append(x3)
    def mul(self):
        # операция умножения
        x1 = self.pop(-1)
        x2 = self.pop(-1)
        x3 = x1 * x2
        self.append(x3)
    def div(self):
        # операция целочисленного деления
        x1 = self.pop(-1)
        x2 = self.pop(-1)
        x3 = x1 // x2
        self.append(x3)