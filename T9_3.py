import json
import sys

from T5_1 import *

# Ich hasse Json, also ischs basically eifach abgschriebe vo ihm


def read_json(nom: str):
    with open(nom, "r") as f:
        return json.load(f)


def afficher_json(doc: dict, indentation: int = 2):
    print(f"Affichage du fichier avec indentation {indentation}")
    print(json.dumps(doc, indent=indentation) + "\n")


def creer_produit_json(nom: str) -> list:
    produits = []

    with open(nom, "r") as f:
        d = json.load(f)

        if "produits" not in d:
            print(f"Warning: Le fichier json {nom} ne contient pas de {produits}", file=sys.stderr)
            return produits

        for produit in d["produits"]:
            if produit["nom classe"] == "Produit":
                produits.append(Produit(produit["nom"], produit["prix"], produit["donnee migros"]))
            else:
                produits.append(ProduitFrais(produit["nom"], produit["prix"], produit["donne migros"], produit["date"]))
    return produits


if __name__ == '__main__':

    nom = "produits.json"
    
    doc = read_json(nom)
    print(doc)

    afficher_json(doc)
    afficher_json(doc, 4)