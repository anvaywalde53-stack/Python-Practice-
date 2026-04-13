import numpy as np

identity_matrix = np.eye(4)
print("4x4 Identity Matrix:")
print(identity_matrix)
print()

mat1 = np.random.randint(1, 10, (3, 3))
mat2 = np.random.randint(1, 10, (3, 3))

print("Matrix 1 (Random):")
print(mat1)
print("\nMatrix 2 (Random):")
print(mat2)

addition = mat1 + mat2
print("\nMatrix Addition Result:")
print(addition)

multiplication = np.dot(mat1, mat2)
print("\nMatrix Multiplication (Dot Product) Result:")
print(multiplication)
