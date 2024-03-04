import argparse

parser = argparse.ArgumentParser(
    prog="Cambriolage.py",
    description="Enregistre les données dans un fichier"
)

parser.add_argument("-d", "--date", type=str, required=True, help="DD/MM/YYYY")
parser.add_argument("-l", "--lieu", type=str, required=True, help="Ville")
parser.add_argument("-v", "--valeur", type=int, required=True, help="Numéro sans virgule ou '")

args = parser.parse_args()

print(f"Un cambriolage a eu lieu le {args.date} à {args.lieu}. Le montant estimé est de {args.valeur} CHF.")

f = open("cambriolage.txt", "a")
f.write(f"{args.date}, {args.lieu}, {args.valeur} \n")
f.close()