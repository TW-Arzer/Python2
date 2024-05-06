from functools import reduce
import sys

list = list(map(lambda x: int(x), sys.argv[1:-1]))

def multiplication():
    x = reduce(lambda x, y: x*y, list)
    return x

def addition():
    x = reduce(lambda x,y: x+y, list)
    return x

def subraction():
    x = reduce(lambda x,y: x-y, list)
    return x

def division():
    x = reduce(lambda x, y: x/y, list)
    return x

if sys.argv[-1] == "*":
    print(multiplication())
elif sys.argv[-1] == "+":
    print(addition())
elif sys.argv[-1] == "-":
    print(subraction())
elif sys.argv[-1] == "/":
    print(division())
else:
    print(f"Le symbol {sys.argv[:-1]} n'est pas implemente")