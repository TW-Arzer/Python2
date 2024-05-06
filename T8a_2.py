import re

pattern = re.compile(r'^(?P<prenom>[a-z-]+)\.(?P<nom>[a-z_]+)(?:[0-9]*)@(?P<institution>[a-z]+)\.ch$')


def match_email(s):
    match = pattern.match(s)
    if match:
        prenom = match.group("prenom").replace("_", " ").title()
        nom = match.group("nom").title()
        institution = match.group("institution").upper()
        return f"Prénom: {prenom}, Nom: {nom}, Institution: {institution}"

    else:
        return f"L'adresse {s} n'est pas valide."


if __name__ == '__main__':

    email = ["yannic.luthi@unil.ch", "jean-kevin.huguenin_de_montmorency12@unil.ch", "kevin.muller@epfl.ch"]

    for i in email:
        print(f"{match_email(i)}\n")
