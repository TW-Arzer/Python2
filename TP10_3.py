import sqlite3

db = sqlite3.connect("movies.db")
cursor = db.cursor()


def count_films():
    cursor.execute("SELECT COUNT(DISTINCT TitreVF) AS nb_films FROM films")
    result = cursor.fetchone()
    for i in result:
        return i


def count_realisateurs():
    cursor.execute("SELECT COUNT(DISTINCT Realisateur) AS nb_realisateurs FROM films")
    result = cursor.fetchone()
    for i in result:
        return i


def est_vide():
    for i in cursor.execute("SELECT * FROM films WHERE TitreVo = ''"):
        id, title_vf, title_vo, year, duration, description, director = i
        return f"\n{id}: {title_vf}, {title_vo}\n{year}, {duration}min\n{director}\n{description}\n"


def delete_doublets():
    cursor.execute("SELECT DISTINCT films.TitreVF FROM emprunteurs JOIN films ON emprunteurs.IDFilm = films.ID")


if __name__ == '__main__':
    print(count_films())
    print(count_realisateurs())

    cursor.execute("DELETE FROM films WHERE films.Annee < 1957 OR films.Annee = ''")

    print(count_films())

    print(est_vide())

    cursor.execute("UPDATE films SET TitreVO = TitreVF WHERE TitreVo = ''")

    print(est_vide())

    delete_doublets()
