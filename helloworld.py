import sys
import getopt

def run():
    print('Hello world. dummy edit')
    print(add(3, 5))

   

def add(a, b):
    return a + b


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv, "?")
    print(__name__)
    run()
