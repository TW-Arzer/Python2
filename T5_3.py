
class Crime:
    __total_crimes = 0
    __total_suspect_e_s = {}

    def __init__(self, lieu, date):
        self.__suspects = []
        self.__lieu = str(lieu)
        self.__date = str(date)
        self.__total_suspect_e_s = 0
        Crime.__total_crimes += 1

    def __str__(self):
        suspects_str = '\n'.join(self.__suspects)
        return f"Crime ayant eu lieu à {self.__lieu}, le {self.__date}.\nLes suspect.e.s sont: \n{suspects_str}"

    def get_lieu(self):
        return self.__lieu

    def get_date(self):
        return self.__date

    def get_suspects(self):
        return self.__suspects

    @classmethod
    def get_total_crime(cls):
        return cls.__total_crimes

    def set_lieu(self, lieu):
        self.__lieu = lieu

    def set_date(self, date):
        self.__date = date

    def ajouter_suspect(self, suspect):
        self.__suspects.append(suspect)
        Crime.__total_suspect_e_s[suspect] = Crime.__total_suspect_e_s.get(suspect, 0) + 1

    @classmethod
    def afficher_total_suspect_e_s(cls):
        print("La totalité de suspect_e_s est: ")
        for suspect, count in cls.__total_suspect_e_s.items():
            print(f"\n\t- {suspect}: {count} crimes")


class Meutre(Crime):
    __total_meutre = 0

    def __init__(self, lieu, date, victime):
        super().__init__(lieu, date)
        self.__victime = str(victime)
        Meutre.__total_meutre += 1

    def get_victime(self):
        return self.__victime

    def set_victime(self, victime):
        self.__victime = victime

    def __str__(self):
        return f"{super().__str__()}\nLe victim.e est: \n{self.__victime}"


class Vol(Crime):
    __total_vol = 0

    def __init__(self, lieu, date, valeur):
        super().__init__(lieu, date)
        self.__valeur = int(valeur)
        Vol.__total_vol += 1

    def get_valeur(self):
        return self.__valeur

    def set_valeur(self, valeur):
        self.__valeur = valeur

    def __str__(self):
        return f"{super().__str__()}\nLe valeur de la vol est: \nCHF {self.__valeur}"


if __name__ == "__main__":
    c1 = Meutre("Lausanne", "24/02/2022", "Hansruedi")
    c1.ajouter_suspect("F. Scott Fitzgerald")
    c1.ajouter_suspect("William Shakespeare")
    c1.ajouter_suspect("Arthur Conan Doyle")
    c1.ajouter_suspect("Charles Dickens")
    c1.ajouter_suspect("Ernest Hemingway")

    c2 = Crime("Crissier", "10/08/2020")
    c2.ajouter_suspect("F. Scott Fitzgerald")
    c2.ajouter_suspect("Tom Clancy")
    c2.ajouter_suspect("Arthur Conan Doyle")

    c3 = Crime("Zürich", "18/05/2023")
    c3.ajouter_suspect("Arthur Conan Doyle")
    c3.ajouter_suspect("Charles Dickens")
    c3.ajouter_suspect("Chris Carter")

    print(c1)
    print(c1.afficher_total_suspect_e_s())
