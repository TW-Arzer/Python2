class Livre:

    def __init__(self, auteur, titre, ane, genre):
        self.__auteur = auteur
        self.__titre = titre
        self.__ane = int(ane)
        self.__genre = genre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_titre(self, titre):
        self.__titre = titre

    def set_ane(self, ane):
        self.__ane = ane

    def set_genre(self, genre):
        self.__genre = genre

    def get_auteur(self):
        return self.__auteur

    def get_titre(self):
        return self.__titre

    def get_ane(self):
        return self.__ane

    def get_genre(self):
        return self.__genre

    def __str__(self):
        return f"{self.__titre} de {self.__auteur}, publié en {self.__ane}"


class Bibliotheque:

    def __init__(self, nom):
        self.nom = nom
        self.livre_par_genre = {}

    def ajout_livre(self, livre):
        if livre.get_genre() in self.livre_par_genre:
            self.livre_par_genre[livre.get_genre()].append(livre)
        else:
            self.livre_par_genre[livre.get_genre()] = [livre]

    def show_genre(self, genre):
        if genre in self.livre_par_genre:
            print(f"Livres du genre {genre}:\n")
            for i in self.livre_par_genre[genre]:
                print(f"\t- {i}\n")
        else:
            print(f"Pas des livres du genre {genre}")

    def __str__(self):
        genres_disponibles = ", ".join(self.livre_par_genre.keys())
        return f"Bibliothèque {self.nom}. Genres disponibles: {genres_disponibles}"


if __name__ == "__main__":
    b1 = Bibliotheque("Staat")
    b2 = Bibliotheque("Uni")

    l1 = Livre("F. Scott Fitzgerald", "The Great Gatsby", 1925, "Roman")
    l2 = Livre("Mary Shelley", "Frankenstein", 1818, "Roman")

    b1.ajout_livre(l1)
    b1.ajout_livre(l2)

    b1.show_genre("Roman")
    print(b1)
