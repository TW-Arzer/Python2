import sqlite3

db = sqlite3.connect("livre.db")
cursor = db.cursor()

for row in cursor.execute("SELECT * FROM 'livres' WHERE nom_auteur = 'Steinbeck'"):
	print(row)
print("\n\n")

print(cursor.description)

field_names = [x[0] for x in cursor.description]
print(field_names)

auteur = input("Entrer le nom d'un auteur: ")
records = tuple(cursor.execute("SELECT * FROM 'livres' WHERE nom_auteur = ?", (auteur,)))

for record in records:
	for i in range(len(record)):
		print(f"{field_names[i]} = {record[i]} ,", end="")
print()


for record in records:
	for (name, value) in zip(field_names, record):
		print(f"{name} = {value}, ", end = "")
		
annee_debut = int(input("Année de début: "))
annee_fin = int(input("Année de fin: "))

records = cursor.execute("SELECT * FROM 'livres' WHERE année > ? AND année < ?", (annee_debut, annee_fin))

for record in records:
	print(record)
print()
	

	
	
db.commit()

db.close()
