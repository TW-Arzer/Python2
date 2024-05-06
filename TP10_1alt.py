import pandas as pd
import sqlite3

db = sqlite3.connect("livre.db")
df_livres = pd.read_sql("SELECT * FROM livres", db, index_col="id")


a = df_livres[df_livres["nom_auteur"] == "Steinbeck"]
b = len(a)

print(a)
print(f"Nombre des livres de Steinbeck: {b}")
print()

c = df_livres[(1950 <= df_livres["année"]) & (df_livres["année"] < 2000)]

print(c)
print()

d = df_livres.sort_values(by="année", ascending=False).iloc[0:3]

print(d)
print()

e = df_livres[df_livres["année"] < 2000].sort_values(by="année").iloc[0]

print(e)
print()

f = df_livres[df_livres["année"] > 1950].sort_values(by="année").iloc[0]

print(f)
print()

g = df_livres.sort_values(by="nom_auteur")[["prenom_auteur", "nom_auteur"]]

print(g)
print()

h = df_livres[["prenom_auteur", "nom_auteur"]].drop_duplicates()

print(h)

db.close()
