from bs4 import BeautifulSoup


class Product:

    def __init__(self, name, prix, bitcoin, vendeur, categorie):
        self._name = name
        self._prix = prix
        self._bitcoin = bitcoin
        self._vendeur = vendeur
        self._categorie = categorie

    def __str__(self):
        return f"Name: \033[95m{self._name}\033[0m,\nPrice: {self._prix},\nBitcoin: {self._bitcoin},\nVendor: {self._vendeur},\
        \nCategory: \033[34m{self._categorie}\033[0m\n\n"

    @staticmethod
    def double_space(string):
        while "  " in string:
            string = string.replace("  ", " ")
        return string


if __name__ == '__main__':

    with open("Acropolis.html", "r", encoding="utf-8") as f:
        source = f.read()

    document = BeautifulSoup(source, "html.parser")
    produits = document.select("html > body > div > div.row > div > div > table > tbody > tr")
    print(len(produits))

    list_produits = []
    for prod in produits:
        name = prod.select("td > div > h4.heading > a")[0].text
        prix = Product.double_space(prod.select("td.price > h4")[0].text.replace("\n", ""))
        bitcoin = prod.select("td.price > h4")[1].text.strip()
        vendeur = prod.select("td > div > h5 > a")[3].text
        categorie = " > ".join(map(lambda x: x.text, prod.select("td > div > h5 > span > a")))
        list_produits.append(Product(name, prix, bitcoin, vendeur, categorie))

    for i in list_produits:
        print(i)