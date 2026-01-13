import math
import random
import ctypes

def py_is_prime(n: int) -> bool:
    if n <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime

def test_is_prime(shared_lib):
    clib = shared_lib
    # ensure ctypes signature
    clib.isPrime.argtypes = [ctypes.c_int]
    clib.isPrime.restype = ctypes.c_bool

    # random numbers
    rnd = random.Random(0)
    nums = [rnd.randint(-20, 100) for _ in range(100)]

    # create the "arrays" using Python and the C library
    py_results = [py_is_prime(n) for n in nums]
    c_results = [bool(clib.isPrime(n)) for n in nums]

    # compare element-wise
    for n, py_res, c_res in zip(nums, py_results, c_results):
        assert py_res == c_res, f"Mismatch for n={n}: solution={py_res}, your answer={c_res}"







