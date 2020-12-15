import math
import numpy as np
import re

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

class CalcParser:

    def __str_parser__(string, number_occu):
        number_re = re.compile('\d+')
        ele_op_re = re.compile('\)\s[*+-/]\s\(')
        ele_val_find = re.findall(ele_op_re, string)
        if not ele_val_find:
            pow_pos = string.find("^")
            abs_pos = string.find("abs")
            if pow_pos != -1:
                values = re.findall(number_re, string)
                if number_occu:
                    values = number_occu
                real_num = float(values[0])
                imag_num = float(values[1])
                pow_val  = float(values[2])
                return Complex(real_num, imag_num), pow_val
            if abs_pos != -1:
                values = re.findall(number_re, string)
                if number_occu:
                    values = number_occu
                real_num = float(values[0])
                imag_num = float(values[1])
                return Complex(real_num, imag_num)
        else:
            values = re.findall(number_re, string)
            if number_occu:
                values = number_occu
            real_num_1 = float(values[0])
            imag_num_1 = float(values[1])
            real_num_2 = float(values[2])
            imag_num_2 = float(values[3])
            oper_sign = re.findall(ele_op_re, string)
            return Complex(real_num_1, imag_num_1), Complex(real_num_2, imag_num_2), oper_sign


print("Enter equation in format (a + b) <operation sign> (c + d) ")
print("a is a real part of complex number and b is an imaginary part")
print("You can do given operations: +, -, *, /, ^, abs")
print("Format for power: (a + b)^n. n is a real number")
print("Format for abs: abs((a + b))")
print("Square root of number: sqrt(number)")

input = input("Equation: ")
print(f"Entered equation {input}")

number_all = list()

number_regex = re.compile('\d+')
occu = [m.start() for m in re.finditer('sqrt', input)]
if occu:
    number_occu = [float(i) for i in re.findall(number_regex, input)]
else:
    number_occu = []
if occu:
    all_val = list()
    for val in occu:
        new_str = input[val+5:]
        close_brack = new_str.find(")")
        number = new_str[0:close_brack]
        number_all.append(float(number))
    number_all_sqrt = list()
    for num in number_all:
        number_all_sqrt.append(math.sqrt(num))

    if len(number_all) != len(number_occu):
        iter = 0
        for i in range(0, len(number_occu)):
            for j in range(0, len(number_all)):
                if number_all[j] == number_occu[i]:
                    number_occu[i] = number_all_sqrt[j]
                    iter = iter + 1
                    if iter == len(number_all):
                        break
            if iter == len(number_all):
                break


def main():
    if input.find("^") != -1:
        comp_1, base = CalcParser.__str_parser__(input, number_occu)
        comp_res = comp_1 ** base
        print(f"Result: {comp_res}")
    elif input.find("abs") != -1:
        comp_1 = CalcParser.__str_parser__(input, number_occu)
        comp_res = abs(comp_1)
        print(f"Result: {comp_res}")
    else:
        comp_1, comp_2, oper_sign = CalcParser.__str_parser__(input, number_occu)
        if '+' in oper_sign[0]:
            comp_res = comp_1 + comp_2
            print(f"Result: {comp_res}")
        elif '-' in oper_sign[0]:
            comp_res = comp_1 - comp_2
            print(f"Result: {comp_res}")
        elif '*' in oper_sign[0]:
            comp_res = comp_1 * comp_2
            print(f"Result: {comp_res}")
        elif '/' in oper_sign[0]:
            comp_res = comp_1 / comp_2
            print(f"Result: {comp_res}")


if __name__ == "__main__":
    main()



