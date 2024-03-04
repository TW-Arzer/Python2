import argparse
import math

parser = argparse.ArgumentParser(
    prog="logarithme.py",
    description="Faire la logarithme dans un chiffre"
)

parser.add_argument("-v", "--verbose", action="store_true", help="Affice les détails du programme", default=False)
parser.add_argument("-n", "--chiffre", type=int, required=True)
parser.add_argument("-b", "--base", type=int, default=2.71828, required=False)
args = parser.parse_args()

try:
    x = math.log(args.chiffre, args.base)
    print(round(x, 3))
except ValueError:
    print("Logarithme n'est pas possible ici")
