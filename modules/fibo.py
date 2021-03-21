# Fibonacci numbers module
"""
  from fibo import *
  from fibo import fib as fibonacci
"""


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# to run this module as script:
# $ python fibo.py <arguments>
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
