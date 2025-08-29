"""
High Performance Programming

Profile and optimize your Python code for performance.

Test Case:
Recursive Problems
https://www.datacamp.com/tutorial/recursion-in-python


Solution:

1)
Dynamic programming
@cache
https://docs.python.org/3/library/functools.html#functools.cache
@lru_cache(maxsize=None)  # Least Recently Used" (LRU)-Cache-Strategie
https://docs.python.org/3/library/functools.html#functools.lru_cache

2)
Concurrency
https://docs.python.org/3/library/concurrency.html
GIL (global interpreter lock)
https://docs.python.org/3/whatsnew/3.13.html#free-threaded-cpython

threading
multiprocessing
https://docs.python.org/3/library/threading.html
https://docs.python.org/3/library/multiprocessing.html
https://docs.python.org/3/library/asyncio.html

3)
Pypy
https://www.pypy.org/

4)
Cython
https://cython.org/
https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html

5)
NumPy
https://en.wikipedia.org/wiki/Array_programming

Numba
https://numba.pydata.org/
https://numba.readthedocs.io/en/stable/user/5minguide.html
Issue with uv
https://github.com/astral-sh/uv/issues/7020

6)
Taichi
https://www.taichi-lang.org/ 
"""

from functools import cache, lru_cache

#from numba import njit
#import taichi as ti

"""
Logging:
https://docs.python.org/3/howto/logging.html
https://docs.python.org/3/howto/logging-cookbook.html
https://docs.python.org/3/library/logging.html
"""
import logging
logger = logging.getLogger("template")

import time
#import asyncio


def delta_time(f):
    """ deltatime Decorator for Profiling """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)  # execute wrapped function
        stop_time = time.time()
        elapsed_time = stop_time - start_time
        print(f"delta_time (dt) = {elapsed_time}")
        return result
    return wrapper


#@delta_time
def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion with caching.
    Args:
        n (int): The position in the Fibonacci sequence.
    """
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterative(n: int) -> int:
    """Calculate the nth Fibonacci number using an iterative approach with caching.
    Args:
        n (int): The position in the Fibonacci sequence."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@cache
def fibonacci_cached(n: int) -> int:
    """Calculate the nth Fibonacci number using recursion with caching.
    Args:
        n (int): The position in the Fibonacci sequence."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


@cache
def fibonacci_iterative_cached(n: int) -> int:
    """Calculate the nth Fibonacci number using an iterative approach with caching.
    Args:
        n (int): The position in the Fibonacci sequence."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


#@njit(nopython=True)
def fibonacci_numba(n: int) -> int:
    """Calculate the nth Fibonacci number using Numba for JIT compilation.
    Args:
        n (int): The position in the Fibonacci sequence."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_numba(n - 1) + fibonacci_numba(n - 2)


#@ti.kernel
def fibonacci_taichi(n: int) -> int:
    """Calculate the nth Fibonacci number using Taichi for parallel computation.
    Args:
        n (int): The position in the Fibonacci sequence."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib = ti.field(int, shape=n + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


def main():
    """Main function to demonstrate the Fibonacci calculation."""
    n = 33     # non-cached recursive solution
    #n = 499    # max rekursion depth for cached recursive solution
    #n = 10000  # iterative solution doesn't need to be cached and is the => fastest solution
    #n = 100000 # ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit


    # recursion, no-cache ----------------------
    # n =  36 done in 5 seconds
    # n =  37 done in 8 seconds
    # n =  38 done in 13 seconds
    start_time = time.time()
    print(f"Fibonacci({n}) recursive without caching: \t{fibonacci(n)} (in {(time.time() - start_time):.6f} seconds)")

    # iterative, no-cache ----------------------
    # n = 5000 done in 0.001 seconds
    start_time = time.time()
    print(f"Fibonacci({n}) iterative without caching: \t{fibonacci_iterative(n)} (in {(time.time() - start_time):.6f} seconds)")

    # recursion, cached ------------------------
    # n = 300 done in 0.001 seconds
    # n = 499 done in 0.001 seconds
    # n = 500 RecursionError: maximum recursion depth exceeded
    # https://stackoverflow.com/questions/74296005/recursion-error-while-trying-to-write-an-memoization-decorator
    # use for-loop instaed of recursion
    start_time = time.time()
    print(f"Fibonacci({n}) recursive with    caching: \t{fibonacci_cached(n)} (in {(time.time() - start_time):.6f} seconds)")

    # iterative, cached ------------------------
    # n = 5000 done in 0.001 seconds
    start_time = time.time()
    print(f"Fibonacci({n}) iterative with    caching: \t{fibonacci_iterative_cached(n)} (in {(time.time() - start_time):.6f} seconds)")

    # numba ------------------------------------
    start_time = time.time()
    #print(f"Fibonacci({n}) with Numba: \t{fibonacci_numba(n)} (in {(time.time() - start_time):.6f} seconds)")

    # taichi -----------------------------------
    #ti.init()
    start_time = time.time()
    #print(f"Fibonacci({n}) with Taichi: \t{fibonacci_taichi(n)} (in {(time.time() - start_time):.6f} seconds)")


if __name__ == "__main__":
    main()

