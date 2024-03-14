import math


class Figure:

    def __init__(self):
        raise NotImplementedError("Figure doit être abstraite")

    def get_aire(self) -> float:
        raise NotImplementedError("Figure doit être abstraite")

    def get_perimetre(self) -> float:
        raise NotImplementedError("Figure doit être abstraite")

    def rapport(self) -> float:
        if not self.get_perimetre() == 0:
            return self.get_aire() / self.get_perimetre()
        else:
            raise ZeroDivisionError("Le périmètre ne peut pas être zéro")

    def __str__(self):
        return f"Figure avec une aire de {self.get_aire()} et périmètre de {self.get_perimetre()}"

    def est_cercle(self) -> bool:
        return isinstance(self, Cercle)

    def est_polygon(self) -> bool:
        if isinstance(self, Carre) or isinstance(self, Rectangle):
            return True
        return False


class Rectangle(Figure):

    def __init__(self, long, larg):
        self.__long = float(long)
        self.__larg = float(larg)

    def __str__(self):
        return f"Rectangle ({self.__long}x{self.__larg})"

    def get_aire(self) -> float:
        return self.__larg * self.__long

    def get_perimetre(self) -> float:
        return self.__larg * 2 + self.__long * 2


class Carre(Figure):

    def __init__(self, long):
        self.__long = float(long)

    def get_aire(self) -> float:
        return self.__long ** 2

    def get_perimetre(self) -> float:
        return self.__long * 4

    def __str__(self):
        return f"Carré ({self.__long}x{self.__long})"


class Ellipse(Figure):

    def __init__(self, rayon_grande, rayon_petite):
        self.__rayon_grande = float(rayon_grande)
        self.__rayon_petite = float(rayon_petite)

    def get_aire(self) -> float:
        return math.sqrt(self.__rayon_grande ** 2 - self.__rayon_petite ** 2)

    def get_perimetre(self) -> float:
        return math.pi * math.sqrt(2 * (self.__rayon_grande ** 2 + self.__rayon_petite ** 2))

    def __str__(self):
        return f"Ellipse ({self.__rayon_grande}x{self.__rayon_petite})"


class Cercle(Figure):

    def __init__(self, rayon):
        self.__rayon = float(rayon)

    def get_aire(self) -> float:
        return math.pi * self.__rayon ** 2

    def get_perimetre(self) -> float:
        return 2 * math.pi * self.__rayon

    def __str__(self):
        return f"Cercle ({self.__rayon})"


if __name__ == "__main__":
    c = Cercle(6)
    e = Ellipse(6, 3)
    ca = Carre(6)
    r = Rectangle(6, 3)

    print(c)
    print(e)
    print(ca)
    print(r)

    print(c.get_perimetre())
    print(c.get_aire())
    print(e.get_perimetre())
    print(e.get_aire())
    print(ca.get_perimetre())
    print(ca.get_aire())
    print(r.get_perimetre())
    print(r.get_aire())

    print(c.est_cercle())
    print(c.est_polygon())
