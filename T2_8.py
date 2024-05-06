import argparse

parser = argparse.ArgumentParser(
    prog="mon_fichier.py"
)

parser.add_argument("-i", "--entier", help="Un entier positif", type=int, required=True)
parser.add_argument("-s", "--chaine", help="Un chaine de caracteres", type=str)

args = parser.parse_args()

if args.chaine is not None:
    print(f"s='{args.chaine}', i={args.entier}")
else:
    print(f"i={args.entier}")