import sqlite3
import csv


def dict_factory(cursor, row):
    return dict([(col[0], row[idx]) for idx, col in enumerate(cursor.description)])


if __name__ == '__main__':
    with open("villes.csv", "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        list_villes = list(csvreader)

    db = sqlite3.connect("population.db")
    db.row_factory = dict_factory
    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS villes_pop")
    cursor.execute("CREATE TABLE villes_pop (id INTEGER PRIMARY KEY AUTOINCREMENT, region TEXT NOT NULL, code INTEGER "
                   "NOT NULL, commune TEXT NOT NULL, population INTEGER NOT NULL)")

    cursor.executemany("INSERT INTO villes_pop (region, code, commune, population) VALUES (?,?,?,?)", list_villes[1:])

    seuil = int(input("Seuil de population: "))

    for row in cursor.execute("SELECT * FROM villes_pop WHERE population > ?", (seuil,)):
        print(f"Commune: {row['commune']}, Population: {row['population']}")

    db.commit()
    db.close()
