from bs4 import BeautifulSoup


class Product:

    def __init__(self, name, prix, bitcoin, vendeur, categorie):
        self._name = name
        self._prix = prix
        self._bitcoin = bitcoin
        self._vendeur = vendeur
        self._categorie = categorie

    def __str__(self):
        return f"Name: {self._name},\nPrice: {self._prix},\nBitcoin: {self._bitcoin},\nVendor: {self._vendeur},\
        \nCategory: {self._categorie}\n\n"


if __name__ == '__main__':

    with open("Acropolis_modif.html", "r", encoding="utf-8") as f:
        source = f.read()

    document = BeautifulSoup(source, "html.parser")

    produits = document.select("html > body > div.body > div.row > div.main_page > div.products > table > tbody > tr")
    print(f"{len(produits)}\n")

    list_produits = []
    for prod in produits:
        name = prod.select("td.description > div.description > h4.heading > a")[0].text
        prix = prod.select("td.price > h4")[0].text.strip()
        bitcoin = prod.select("td.price > h4")[1].text.strip()
        vendeur = prod.select("td.description > div.description > h5 > a")[0].text
        catgeorie = prod.select("td.description > div.description > h5")[1].text[11:]
        list_produits.append(Product(name, prix, bitcoin, vendeur, catgeorie))

    for i in list_produits:
        print(i)