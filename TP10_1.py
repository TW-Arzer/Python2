import sqlite3

db = sqlite3.connect("livre.db")
cursor = db.cursor()

a = cursor.execute("SELECT * FROM 'livres' WHERE nom_auteur = 'Steinbeck'")


nb_steinbeck = 0
for row in a:
	print(row)
	nb_steinbeck += 1
	
print(f"{nb_steinbeck}\n\n")


c = cursor.execute("SELECT * FROM 'livres' WHERE année > 1950 ORDER BY année DESC LIMIT 3")

for row in c:
	print(row)
print("\n\n")


e = cursor.execute("SELECT * FROM 'livres' WHERE année < 2000 ORDER BY année DESC LIMIT 1")

for row in e:
	print(row)
print("\n\n")


f = cursor.execute("SELECT * FROM 'livres' WHERE année >1950 ORDER BY année ASC LIMIT 1")

for row in f:
	print(row)
print("\n\n")	


g = cursor.execute("SELECT * FROM 'livres' ORDER BY nom_auteur DESC")

for row in g:
	print(row)
print("\n\n")	


h = cursor.execute("SELECT DISTINCT prenom_auteur, nom_auteur  FROM 'livres'")

for row in h:
	print(row)
print("\n\n")


cursor.execute("INSERT INTO 'auteurs' VALUES (6, 'F.Scott', 'Fitzgerald', 'non')")

for row in cursor.execute("SELECT * FROM 'auteurs'"):
	print(row)
print("\n\n")


cursor.execute("DELETE FROM 'auteurs' WHERE id = 6")

for row in cursor.execute("SELECT * FROM 'auteurs'"):
	print(row)
print("\n\n")



db.commit()

db.close()
