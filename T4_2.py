__reduction_generale = 0
__delai_expiration_reduction = 1


class Produit:

    def __init__(self, nom, prix, reduction):
        self.__nom = nom
        self.__reduction = int(reduction)
        if prix < 0.0:
            raise ValueError(
                "Pas de prix inférieur à 0 svp"
            )
        self.__prix = round(float(prix), 2)

    @staticmethod
    def verification_reduction(reduction):
        if reduction > 100 or reduction < 0:
            raise ValueError(
                "Les réductions doivent être comprises entre 0 et 100 (%)"
            )

    def set_reduction(self, reduction):
        reduction = float(reduction)
        self.__class__.verification_reduction(reduction)
        self.__reduction = reduction

    def get_prix_initial(self):
        return self.__prix

    @classmethod
    def set_reduction_generale(cls, reduction):
        reduction = float(reduction)
        cls.verification_reduction(reduction)
        cls.__reduction_generale = reduction

    def get_prix_courant(self):
        return round(self.__reduction_generale * (1.0 - self.__reduction_generale / 100) *
                     (1.0 - self.__reduction / 100), 2)

    def __str__(self):
        new = self.get_prix_courant()
        old = self.get_prix_initial()
        return f"[Produit] {self.__nom} ({new} CHF {f', était à {old} CHF' if old != new else ''}"


