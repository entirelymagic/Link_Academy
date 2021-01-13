class Calculator():
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def add(self):
        return self.operand1 + self.operand2

    def mul(self):
        return self.operand1 * self.operand2

    def max(self):
        return max(self.operand1, self.operand2)


operatia1 = Calculator(8, 31)
print(operatia1.add())
print(operatia1.max())
