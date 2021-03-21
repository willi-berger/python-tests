import sys
import getopt

opts, args = getopt.getopt(sys.argv, "?")

def add(a, b):
    return a + b

print('Hello world')
print(add(3, 5))