import argparse
import math

parser = argparse.ArgumentParser(
    prog="Racine.py"
)

parser.add_argument("-n", "--entier", help="Entier pour calculer la fonction racine carrée", required=True, type=int)
parser.add_argument("-o", "--output", help="Enregistre le résultat dans un fichier", action="store_true")

args = parser.parse_args()

if args.output:
    f = open("resultat.txt", "a")
    f.write(f"Racine carrée de {args.entier} est égal à {math.sqrt(args.entier)} \n")
    f.close()
    print(math.sqrt(args.entier))
else:
    print(math.sqrt(args.entier))