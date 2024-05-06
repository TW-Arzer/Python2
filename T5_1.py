class Produit:
    __reduction_generale = 0
    __delai_expiration_reduction = 1

    def __init__(self, nom, prix, donnee_migros):
        self.__nom = nom
        self.__reduction = 0
        if prix < 0.0:
            raise ValueError(
                "Pas de prix inférieur à 0 svp"
            )
        self.__prix = round(float(prix), 2)
        self.__donnee = int(donnee_migros)
        if self.__donnee > 365 or self.__donnee < 0:
            raise ValueError("'donne_migros' doit être compris entre 0 et 365")

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
        prix_return_general = self.__prix * (1.0 - self.__class__.__reduction_generale / 100)
        prix_final = prix_return_general * (1.0 - self.__reduction / 100)
        return round(prix_final, 2)

    def __str__(self):
        new = self.get_prix_courant()
        old = self.get_prix_initial()
        if not isinstance(self, ProduitFrais):
            return f"[Produit] {self.__nom} ({new} CHF{f', était à {old} CHF' if old != new else ')'}"
        else:
            return f"[ProduitFrais] {self.__nom} ({new} CHF{f', était à {old} CHF' if old != new else ')'}"

    def est_expire(self, date):
        return self.__donnee < date

    def expire_bientot(self, date):
        return self.__donnee - date <= self.get_delai_expiration_reduction()

    @classmethod
    def set_expiration_reduction(cls, delai):
        delai = int(delai)
        if delai < 0:
            raise ValueError("Le délai d'expiration des réductions doit être supérieur à 0")
        cls.__delai_expiration_reduction = delai

    @classmethod
    def get_delai_expiration_reduction(cls):
        return cls.__delai_expiration_reduction


class ProduitFrais(Produit):
    __delai_expiration_reduction = 3

    def __init__(self, nom, prix, date_emballage, donnee_migros):
        super().__init__(nom, prix, donnee_migros)
        self.__date_emballage = int(date_emballage)

    def __str__(self):
        return f"{super(ProduitFrais, self).__str__()}, date d'emballage: {self.__date_emballage}"

    @classmethod
    def get_delai_expiration_reduction(cls):
        return cls.__delai_expiration_reduction


class Supermarche:
    __EXPIRATION_REDUCTION = 50

    def __init__(self):
        self.__produits = []

    def __str__(self):
        return '[Supermarche]\n' + '\n'.join([f"- {i}" for i in self.__produits])

    def ajouter(self, produit):
        if not isinstance(produit, Produit):
            raise TypeError("Seules des produits de type Produit svp")
        self.__produits.append(produit)

    def mettre_a_jour(self, date):
        self.__produits = [i for i in self.__produits if not i.est_expire(date)]

        for j in self.__produits:
            if j.expire_bientot(date):
                j.set_reduction(self.__class__.__EXPIRATION_REDUCTION)


if __name__ == "__main__":
    rayon = Supermarche()
    pf = ProduitFrais("Saumon", 10.0, 6, 2)
    print(pf)
    rayon.ajouter(ProduitFrais("Saumon", 10.0, 6, 2))
    rayon.ajouter(ProduitFrais("Pain", 3.0, 2, 1))
    rayon.ajouter(Produit("Sauce", 6.0, 10))
    print(rayon)
    print()
    for date in range(12):
        print("Day " + str(date))
        if date == 4:
            Produit.set_reduction_generale(20)
        if date == 7:
            Produit.set_reduction_generale(0)
        rayon.mettre_a_jour(date)
        print(rayon)
