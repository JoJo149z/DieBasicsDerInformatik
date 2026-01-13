import ctypes
'''
SOURCE: https://www.geeksforgeeks.org/dsa/matrix-exponentiation/
'''

MOD = 10**9 + 7

# function to multiply two 2x2 Matrices
def multiply(A, B):
    # Matrix to store the result
    C = [[0, 0], [0, 0]]

    # Matrix Multiply
    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD
    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD
    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD

    # Copy the result back to the first matrix
    A[0][0] = C[0][0]
    A[0][1] = C[0][1]
    A[1][0] = C[1][0]
    A[1][1] = C[1][1]

# Function to find (Matrix M ^ expo)
def power(M, expo):
    # Initialize result with identity matrix
    ans = [[1, 0], [0, 1]]

    # Fast Exponentiation
    while expo:
        if expo & 1:
            multiply(ans, M)
        multiply(M, M)
        expo >>= 1

    return ans


def nthFibonacci(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    M = [[1, 1], [1, 0]]
    # F(0) = 0, F(1) = 1
    F = [[1, 0], [0, 0]]

    # Multiply matrix M (n - 1) times
    res = power(M, n - 1)

    # Multiply Resultant with Matrix F
    multiply(res, F)

    return res[0][0] % MOD

def test_fib(shared_lib):
    shared_lib.fibonacci.argtypes = [ctypes.c_int]
    shared_lib.fibonacci.restype = ctypes.c_int

    nums = [x for x in range(10)]

    # create the "arrays" using Python and the C library
    py_results = [nthFibonacci(n) for n in nums]
    c_results = [int(shared_lib.fibonacci(n)) for n in nums]

    # compare element-wise
    for n, py_res, c_res in zip(nums, py_results, c_results):
        assert py_res == c_res, f"Mismatch for n={n}: solution={py_res}, your answer={c_res}"