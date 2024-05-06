import pandas as pd
import sqlite3

db = sqlite3.connect("livre.db")
df_auteurs = pd.read_sql("SELECT * FROM auteurs", db, index_col="id")
df_livres = pd.read_sql("SELECT * FROM livres", db, index_col="id")
df_livres_ref = pd.read_sql("SELECT * FROM livres_refs", db, index_col="id")


new_author = pd.DataFrame({"prenom_auteur": ["John"], "nom_auteur": ["Tolkien"], "vivant_auteur": ["non"]},
                          index=[df_auteurs.index.max() + 1])

df_auteurs = pd.concat([df_auteurs, new_author])

print(df_auteurs)
print()

df_auteurs = df_auteurs[df_auteurs["nom_auteur"] != "Tolkien"]

print(df_auteurs)
print()


new_livre1 = pd.DataFrame({"titre": ["Le Hobbit"], "type": ["roman"], "nom_auteur": ["Tolkien"], "prenom_auteur": ["John"], "vivant_auteur": ["non"], "année": ["1937"], "langue": ["fr"]}, index=[df_livres.index.max() + 1])
new_livre2 = pd.DataFrame({"titre": ["Les Aventures de Tom Bombadil"], "type": ["roman"], "nom_auteur": ["Tolkien"], "prenom_auteur": ["John"], "vivant_auteur": ["non"], "année": ["1962"], "langue": ["fr"]}, index=[df_livres.index.max() + 2])

df_livres = pd.concat([df_livres, new_livre1, new_livre2])

print(df_livres)
print()

df_livres = df_livres[df_livres["nom_auteur"] != "Tolkien"]

new_livre1_ref = pd.DataFrame({"titre": ["Le Hobbit"], "type": ["roman"], "année": ["1937"], "langue": ["fr"], "id_auteur": ["6"]}, index=[df_livres.index.max() + 1])
new_livre2_ref = pd.DataFrame({"titre": ["Les Aventures de Tom Bombadil"], "type": ["roman"], "année": ["1962"], "langue": ["fr"], "id_auteur": ["6"]}, index=[df_livres.index.max() + 2])

print(df_livres)
print()

df_livres_ref = pd.concat([df_livres_ref, new_livre1_ref, new_livre2_ref])

print(df_livres_ref)
print()

df_livres_ref = df_livres_ref[df_livres_ref["id_auteur"] != "6"]

print(df_livres_ref)

db.close()
