import argparse

import module
import sys
from functools import reduce

# q1

if __name__ == "__main__":
    module.echo("Ceci est un message depuis T2.py")


# q2

def repeat():
    if len(sys.argv[1:]) > 0:
        x = reduce(lambda x, y: x*y, map(int, sys.argv[1:]))
        return f"Multiplication de {sys.argv[1:]} est égal à {x}."
    return None

print(repeat())

# q3

def calculations():
    if len(sys.argv[1:]) > 0:
        try:
            x = reduce(lambda x, y: x/y, map(int, sys.argv[1:]))
            return f"Division de {sys.argv[1:]} est égal à {x}."
        except ZeroDivisionError:
            print("Division par 0 n'est pas possible")
    return None

print(calculations())


# q4

try:
    x = list(map(lambda x: int(x)**2, sys.argv[1:]))
    print(f"Racine carrée de {sys.argv[1:]} est égal à {x}.")
except ValueError:
    print("S'il vous plaît, seulement des chiffres")
finally:
    print("Au revoir!")


# q5

try:
    x = input("S'il vous plaît, ecrire un nombre: ")
    print(int(x)**2)
except ValueError:
    print("S'il vous plaît, seulement des chiffres")


# q6

try:
    x = input("Combien des entiers: ")
    x = int(x)
    l = []
    while x > 0:
        y = input("Ecrire: ")
        l.append(y)
        x -= 1
    z = " ". join(l)
    print(z)
except ValueError:
    print("S'il vous plaît, seulement des chiffres pour entier")


# q7

