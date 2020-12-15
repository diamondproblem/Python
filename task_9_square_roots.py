import numpy as np

coeff_names = ["a", "b", "c"]
coeff = list()
coeff_str = list()

for cof_name in coeff_names:

    in_cof = input("Enter coefficient " + cof_name + ": ")
    if in_cof.isalpha():
        raise Exception("Input has to be numeric!")
    print("Coefficient " + cof_name + " is " + str(in_cof))
    coeff.append(float(in_cof))
    coeff_str.append(in_cof)

print("Solving an equation: y = " + coeff_str[0] + "x^2 + " + coeff_str[1] + "x + " + coeff_str[2])

square_roots = np.roots(coeff)

if square_roots[0] == square_roots[1]:
   print("There is only one square root x0 = " + str(square_roots[0]))
else:
    print("Square roots: x1 = " + str(square_roots[0]) + " x2 = " + str(square_roots[1]))


