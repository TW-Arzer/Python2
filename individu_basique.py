from T6_4 import Observable, Observer, Tabloid


class Individu(Observable):
    def __init__(self, prenom: str, nom: str):
        super().__init__()
        self.__prenom = prenom
        self.__nom = nom

    def epouse(self):
        self.notify_all('Je me marie ! (' + self.__prenom + ' ' + self.__nom + ')')


if __name__ == '__main__':

    robin = Individu("Scherbatsky", "Robin")

    public = Tabloid("Public")
    sun = Tabloid("Sun")

    robin.add_observer(public)
    robin.add_observer(sun)

    robin.epouse()