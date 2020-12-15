import math
import numpy as np


class Complex:

    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        res = Complex(self)
        res.real = (self.real * other.real + self.imag * other.imag)/denominator
        res.imag = (self.imag * other.real - self.real * other.imag)/denominator
        return res

    def __pow__(self, base):
        abs_z = math.sqrt(self.real ** 2 + self.imag ** 2)
        sin_fi = self.imag/abs_z
        cos_fi = self.real/abs_z
        angle_fi = np.arcsin(sin_fi)
        power_abs_z = math.pow(abs_z, base)
        power_arg_cos = math.cos(base * angle_fi)
        power_arg_sin = math.sin(base * angle_fi)
        self.real = power_abs_z ** base * power_arg_cos
        self.imag = power_abs_z * power_arg_sin
        self.real = round(self.real, 2)
        self.imag = round(self.imag, 2)
        if self.real == -0.0:
            self.real = 0.0
        if self.imag == -0.0:
            self.imag = 0.0
        return self

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __neg__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.real}, {self.imag}i"


def main():
    comp_1 = Complex(1, 8)
    comp_2 = Complex(2, 3)
    comp_3 = Complex(math.sqrt(3), 1)

    comp_4 = comp_3 ** 3

    comp_5 = (comp_1)/(comp_2)

    print("Result of exponentiation", comp_4)
    print("Result of division", comp_5)

if __name__ == "__main__":
    main()



