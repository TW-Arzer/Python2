import urllib.parse
import urllib.request
import json
import sys
from datetime import datetime

API_KEY = "YOUR_API_KEY"

if __name__ == '__main__':

    not_found = True

    choix = input("Taper 1 pour faire une recherche en utilisant un nom de ville et 2 pour faire une recherche en "
                  "utilisant des coordonnées GPS: ")

    while not_found:
        try:
            if choix == "1":
                query = input("Chercher météo.\nEntrez le nom de la ville: ")
                parametres = urllib.parse.urlencode({"q": query, "appid": API_KEY, "units": "metric", "lang": "fr"})

            elif choix == "2":
                latitude = input("Entrez la latitude: ")
                longitude = input("Entrez la longitude: ")
                parametres = urllib.parse.urlencode({"lat": latitude, "lon": longitude, "appid": API_KEY,
                                                     "units": "metric", "lang": "fr"})

            else:
                break

            response = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?{parametres}")
            result = json.load(response)

            if "weather" in result:
                prevision = result["weather"][0]["description"]
                temp  = result["main"]["temp"]
                humidity = result["main"]["humidity"]
                nom_ville = result["name"]
                pays = result["sys"]["country"]
                lever = datetime.fromtimestamp(result["sys"]["sunrise"])
                coucher = datetime.fromtimestamp(result["sys"]["sunset"])
                print(f"Prévision: {prevision}, Température: {temp:.2f}, Humidité: {humidity} pour la ville de {nom_ville}, {pays}.")
                print(f"Lever du soleil: {lever}, Coucher du soleil: {coucher}")

                not_found = False

        except Exception as e:
            print(e, file=sys.stderr)
            continue