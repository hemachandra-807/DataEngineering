class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()

print(calc.add(5))         # 5 + 0 + 0 = 5
print(calc.add(5, 3))      # 5 + 3 + 0 = 8
print(calc.add(5, 3, 2))   # 5 + 3 + 2 = 10
