import googlemaps
from datetime import datetime
import html2text

gmaps = googlemaps.Client(key="YOUR_API_KEY")




def get_address():
    address = input("Veuillez entrer une adresse: ")

    geocode_result = gmaps.geocode(address)

    if geocode_result:
        formatted_address = geocode_result[0]["formatted_address"]
        print(f"Addresse identifiée: {formatted_address}")

        while True:
            confirmer = input("Confirmer [y/n]: ")
            if confirmer == "y":
                print("Superb")
                break
            elif confirmer == "n":
                print("Fonction n'implement pas" file=sys.stderr)
            else:
                print("Au schomal y oder n iitipt?")



    else:
        print("Aucune résultat trouve pour cette adresse.")


def distance(depart, arrive):
    now = datetime.now()

    distance_car = gmaps.distance_matrix(depart, arrive, mode="driving", departure_time=now)
    if distance_car['rows'][0]['elements'][0]['status'] == 'OK':
        distance = distance_car['rows'][0]['elements'][0]['distance']['text']
        duration = distance_car['rows'][0]['elements'][0]['duration']['text']
        print(f"The distance between {depart} and {arrive} is {distance} and it takes approximately {duration} by car.")
    else:
        print("Distance and time could not be calculated due to an error with the input addresses or network issues.")

    distance_foot = gmaps.distance_matrix(depart, arrive, mode="bicycling", departure_time=now)
    if distance_foot['rows'][0]['elements'][0]['status'] == 'OK':
        distance = distance_foot['rows'][0]['elements'][0]['distance']['text']
        duration = distance_foot['rows'][0]['elements'][0]['duration']['text']
        print(f"The distance between {depart} and {arrive} is {distance} and it takes approximately {duration}"
              f" by bike.")
    else:
        print("Distance and time could not be calculated due to an error with the input addresses or network issues.")


if __name__ == '__main__':
    depart = get_address()
    arrive = get_address()

    distance(depart, arrive)
