import csv

if __name__ == '__main__':
    dict_admin = {}
    with open("etudiants_admin.csv", "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        for i in csvreader:
            dict_admin[i[0]] = i
    print(dict_admin)

    dict_noms = {}
    with open("etudiants_noms.csv", "r", newline="", encoding="utf-8") as csvfile:
        dial = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        csvreader = csv.DictReader(csvfile, dialect=dial)
        for i in csvreader:
            dict_noms[i["id"].strip()] = (i["nom"].strip(), i["prénom"].strip())
    print(dict_noms)

    l = []
    for i in dict_admin:
        if i in dict_noms:
            l.append({"email": dict_admin[i][1], "nom + prénom": dict_noms[i]})
    print(l)

    with open("etudiants_test.csv", "w", newline="") as csvfile:
        csvwriter = csv.DictWriter(csvfile, ["nom + prénom", "email"], quotechar='"', quoting=csv.QUOTE_ALL)
        csvwriter.writeheader()
        for i in l:
            csvwriter.writerow(i)