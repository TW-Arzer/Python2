
class Individu:
    __personne = []

    def __init__(self, nom, prenom, age=0):
        self._nom = str(nom)
        self._prenom = str(prenom)
        self.__age = age
        self._conjoint = None
        Individu.__personne.append(self)
        print(f"[{self._prenom}] est né")

    def __str__(self):
        return f"{self._prenom} ({self.__age} {f'an)' if self.__age <= 1 else 'ans)'}"

    def get_nom(self):
        return self._nom

    def get_prenom(self):
        return self._prenom

    def get_age(self):
        return self.__age

    def anniversaire(self):
        self.__age += 1

    def __eq__(self, other):
        if self._prenom == other._prenom and self._nom == other._nom and self.__age == other.__age:
            return True
        return False

    @classmethod
    def senior(cls, limit):
        return [i for i in cls.__personne if Individu.get_age(i) > limit]

    def get_gender(self):
        if isinstance(self, Homme):
            return "M"
        elif isinstance(self, Femme):
            return "F"
        else:
            return "undefined"

    def marier(self, other):
        if isinstance(other, Individu) and other is not self and (self._conjoint is None or self._conjoint == "divorce") and (other._conjoint is None or other._conjoint == "divorce"):
            self._conjoint = other
            other._conjoint = self
            print("Congratulations")
            if isinstance(self, Femme) and isinstance(other, Homme):
                self.set_nom_marital(other._nom)
            elif isinstance(other, Femme) and isinstance(self, Homme):
                other.set_nom_marital(self._nom)
        else:
            print("Mariage impossible")

    def est_marie(self):
        if self._conjoint is None or self._conjoint == "divorce":
            return False
        return True

    def divorce(self, other):
        if self._conjoint == other and other._conjoint == self:
            self._conjoint = "divorce"
            other._conjoint = "divorce"
            print("Vous êtes maintenant divorcés")
            if isinstance(self, Femme) and isinstance(other, Homme):
                self.set_nom_divorce()
            elif isinstance(other, Femme) and isinstance(self, Homme):
                other.set_nom_divorce()
        else:
            print("Divorce est seulement possible pour les personnes mariées")


class Femme(Individu):

    def __init__(self, nom, prenom, age=0, nom_marital=""):
        super().__init__(nom, prenom, age)
        self._nom_marital = nom_marital

    def get_nom_marital(self):
        return self._nom_marital

    def set_nom_marital(self, nom_marital):
        self._nom_marital = nom_marital

    def set_nom_divorce(self):
        self._nom_marital = ""

    def __str__(self):
        return f'{self.get_prenom()} {self._nom_marital}{f"-" if self._nom_marital != "" else ""}{self.get_nom()} ' \
               f'({self.get_age()}{f" an)" if self.get_age() <= 1 else " ans)"}'


class Homme(Individu):

    def __init__(self, nom, prenom, age=0):
        super().__init__(nom, prenom, age)


if __name__ == '__main__':
    p1 = Homme("Schmid", "Peter")
    p2 = Individu("Peterhans", "Hanspeter")
    p3 = Femme("Peterhans", "Marie")
    p4 = Individu("Schmid", "Peter")

    print(p1 == p4)
    print(p1)
    p3.anniversaire()
    p3.anniversaire()
    p1.anniversaire()
    p1.anniversaire()
    print(p3)
    print()
    print()

    p1.marier(p3)
    print(p3)
    p1.divorce(p3)

    list = Individu.senior(1)
    for i in list:
        print(i)
