

class Crime:

    def __init__(self, lieu, date):
        self.__suspects = []
        self.__lieu = str(lieu)
        self.__date = str(date)

    def __str__(self):
        suspects_str = '\n'.join(self.__suspects)
        return f"Crime ayant eu lieu à {self.__lieu}, le {self.__date}.\nLes suspect.e.s sont: \n{suspects_str}"

    def get_lieu(self):
        return self.__lieu

    def get_date(self):
        return self.__date

    def get_suspects(self):
        return self.__suspects

    def set_lieu(self, lieu):
        self.__lieu = lieu

    def set_date(self, date):
        self.__date = date

    def ajouter_suspect(self, suspect):
        self.__suspects.append(suspect)

if __name__ == "__main__":
    c1 = Crime("Lausanne", "24/02/2022")
    c1.ajouter_suspect("F. Scott Fitzgerald")
    c1.ajouter_suspect("William Shakespeare")
    c1.ajouter_suspect("Arthur Conan Doyle")
    c1.ajouter_suspect("Charles Dickens")
    c1.ajouter_suspect("Ernest Hemingway")

    print(c1)
