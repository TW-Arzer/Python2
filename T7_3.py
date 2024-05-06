from datetime import *


class Evenement:

    def __init__(self, nom: str, date: datetime, duree: timedelta):
        self.__nom = nom
        self.__date = date
        self.__duree = duree

    def set_nom(self, nom):
        self.__nom = nom

    def set_date(self, date):
        self.__date = date

    def set_duree(self, duree):
        self.__duree = duree

    def get_nom(self):
        return self.__nom

    def get_date(self):
        return self.__date

    def get_duree(self):
        return self.__duree

    def __str__(self):
        date_fin = self.__date + self.__duree
        fin = self.__date + self.__duree
        if self.__date.date() == date_fin.date():
            return f"{self.__nom}, le {datetime.strftime(self.__date, '%d/%m/%Y de %H:%M')} à {datetime.strftime(fin, '%H:%M')}"
        else:
            return f"{self.__nom}, le {datetime.strftime(self.__date, '%d/%m/%Y à %H:%M')}, jusqu\'au {datetime.strftime(fin, '%d/%m/%Y à %H:%M')}"

    def __lt__(self, other):
        if self.__date == other.__date:
            return self.__duree < other.__duree
        return self.__date < other.__date

    def __le__(self, other):
        if self.__date == other.__date:
            return self.__duree <= other.__duree
        return self.__date <= other.__date

    def __gt__(self, other):
        if self.__date == other.__date:
            return self.__duree > other.__duree
        return self.__date > other.__date

    def __ge__(self, other):
        if self.__date >= other.__date:
            return self.__duree >= other.__duree
        return self.__date >= other.__date


class Calendrier:

    def __init__(self):
        self.__evenements = []

    def ajouter_evenements(self, evenement: Evenement):
        self.__evenements.append(evenement)

    def supprimer_evenement(self, evenement: Evenement):
        self.__evenements.remove(evenement)

    def afficher_evenements(self):
        for i in self.__evenements:
            print(i)


if __name__ == '__main__':
    E1 = Evenement("Springbreak", datetime(2024, 4, 5, 12), timedelta(days=14))
    E2 = Evenement("Ka", datetime(2024, 4, 8, 12, 30), timedelta(hours=5))
    E3 = Evenement("Holidays", datetime(2024, 4, 1), timedelta(days=7))
    c1 = Calendrier()

    c1.ajouter_evenements(E1)
    c1.ajouter_evenements(E2)
    c1.ajouter_evenements(E3)

    c1.afficher_evenements()
