 import numpy as np

def get_matrix_input(rows, cols):
    print(f"Enter elements for a {rows}x{cols} matrix (space-separated for each row):")
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        elements.append(row)
    return np.array(elements)

print("--- Matrix A (5x3) ---")
matrix_a = get_matrix_input(5, 3)

print("\n--- Matrix B (3x2) ---")
matrix_b = get_matrix_input(3, 2)

product_matrix = np.dot(matrix_a, matrix_b)

print("\nMatrix A:")
print(matrix_a)
print("\nMatrix B:")
print(matrix_b)
print("\nProduct Matrix (5x2):")
print(product_matrix)
