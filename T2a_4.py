import argparse
from functools import reduce
import sys

d = {"+": lambda x,y: x+y, "*": lambda x,y: x*y, "/": lambda x,y: x/y, "-": lambda x,y: x-y}

parser = argparse.ArgumentParser(
    prog="Calculatrice.py",
    description="Different type d'opérations mathématique"
)

parser.add_argument("-v", "--verbose", help="Afficher avertissements", action="store_true")
parser.add_argument("-n", "--number", help="Nombres à combiner", required=True, type=int, nargs="+")
parser.add_argument("-o", "--operator", help="opératuer à utiliser", required=True, choices=d.keys())

args = parser.parse_args()

if args.verbose:
    print("Mode verbose activé", file=sys.stderr)
    print("%d entiers lus" % len(args.number), file=sys.stderr)

print(reduce(d[args.operator], args.number))