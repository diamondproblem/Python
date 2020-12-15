import numpy as np
import random

dim = random.randint(1, 100)

A = np.random.rand(dim, dim)

determinant_of_arr = np.linalg.det(A)

print(f"Array A {A}")

print(f"\n\nDimensions of A {dim}x{dim}")

print(f"\n\nDetrminant of A {determinant_of_arr}")