#Description: This file contains the polynomial interpolation method.
from sympy import Matrix

def SLSystem(matrix, vector):
    """
    Solve a linear system Ax = b using Gauss-Jordan elimination.
    :param matrix: Coefficient matrix A.
    :param vector: Right-hand side vector b.
    :return: Solution vector x.
    """
    A = Matrix(matrix)
    b = Matrix(vector)
    if A.det() == 0:
        raise ValueError("The matrix is singular and cannot be solved.")
    solution = A.inv() * b
    return [float(val) for val in solution]

def polynomial(table,P):
    """
    Polynomial interpolation using the given table.
    :param table: List of (x, y) points.
    :param P: Value at which to evaluate the polynomial.
    :return: Evaluated polynomial at P.
    """
    n = len(table)
    x = [point[0] for point in table]
    y = [point[1] for point in table]

    # Create the Vandermonde matrix
    matrixA = [[x[i] ** j for j in range(n)] for i in range(n)]
    vectorb = [[y[i]] for i in range(n)]

    # Solve polynomial coefficients
    pc = SLSystem(matrixA, vectorb)
    # Print the polynomial in the correct order (highest degree to constant)
    print("\nThe polynomial:")
    polynomial_str = " + ".join([f"({pc[i]:.10f}) * X^{i}" for i in range(n - 1, -1, -1) if pc[i] != 0])

    # Add the minus sign for negative coefficients
    polynomial_str = polynomial_str.replace("+ -", "- ")

    print(f"P(t) = {polynomial_str}")
    result = 0

    # Flag to print the table once
    if not hasattr(polynomial, "is_printed"):
        polynomial.is_printed = True  # Set the flag after the first print

        print(f"{'Iteration':<10} | {'coeffs':<15} | {'Pi':<10} | {'Partial Result'}")
        print("-" * 50)

        for i in range(n):
            term = pc[i] * (P ** i)
            result += term
            print(f"{i + 1:<10} | {pc[i]:<15.6f} | {P ** i:<10.6f} | {term:<15.6f}")

    result= sum([pc[i] * (P ** i) for i in range(n)])
    return result