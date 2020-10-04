import random


class Calculator:
    def __init__(self, init_value=0.0):
        self.value = init_value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        return Calculator(self.value).add(float(other))

    def __sub__(self, other):
        return Calculator(self.value).add(float(other))

    def __mul__(self, other):
        return Calculator(self.value).multiply(float(other))

    def __pow__(self, power, modulo=None):
        return Calculator(self.value).power(power, modulo=modulo)

    def __truediv__(self, other):
        return Calculator(self.value).divide(float(other))

    def add(self, *args):
        self.value += sum(args)
        return self

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if x == 0:
                raise ValueError("Can not divide a number by 0.")
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self

    def power(self, *args, integer_power=False, modulo=None):
        for x in args:
            self.value = pow(self.value, x, modulo)
            if integer_power:
                self.value = int(self.value + 0.5)
        return self

    def root(self, *args, integer_root=False):
        for x in args:
            self.power(1 / x)
            if integer_root:
                self.value = int(self.value + 0.5)
        return self

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def __iter__(self):
        return self.value


if __name__ == '__main__':
    calc = Calculator(1)
    print((calc * 100.5 - 70) ** 3)
    print((calc * 100.6 - 70) ** 3)

    calculator = Calculator(random.randint(1, 100))
    calculator2 = Calculator(random.randint(1, 100))
    calc3 = calculator + calculator2
    print(calculator, calculator2, calc3)
    print(calculator + calc3)
    print((calc3 + 3) * 123 + 10000000)
    print(Calculator(123) + '321')
    a = Calculator(9)
    print(a ** 123)
    print(a / 2.5)

    # print(calculator.add(1, 2, 3, 5.1).multiply(4, 0.123).subtract(4, 1, -100).divide(5, integer_divide=True))
    # print(Calculator(100) + 10)
    # print(10 + Calculator(12))
    # print(Calculator(123) - Calculator(14))
    # print(Calculator(14) / Calculator(2))
