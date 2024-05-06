class Individu:

    def __init__(self, prenom, nom):
        self.__prenom = prenom
        self.__nom = nom
        self.__age = 0
        print(f"{self.__prenom} {self.__nom} est né")

    def __str__(self):
        if self.__age > 1:
            return f"{self.__prenom} ({self.__age} ans)"
        else:
            return f"{self.__prenom} ({self.__age} an)"

    def get_age(self):
        return self.__age

    def anniversaire(self):
        self.__age += 1
        print(f"Happy Birthday {self.__prenom}! Vous avez maintenant {self.__age} ans.")


if __name__ == "__main__":
    in1 = Individu("Jean", "Paul")
    print(in1.get_age())
    in1.anniversaire()
    print(in1.get_age())
    in1.anniversaire()
    print(in1)
