import csv


if __name__ == '__main__':
    dict_admin = {}
    with open("etudiants_admin.csv", "r", newline="") as f:
        f_read = csv.reader(f, delimiter=";")
        for i in f_read:
            dict_admin[i[0]] = i
            print(i)

    dict_noms = {}
    with open("etudiants_noms.csv", "r", newline="") as f:
        f_read = csv.reader(f, delimiter=",")
        header = True
        for i in f_read:
            if header:
                header = False
                continue
            dict_noms[i[2]] = i

    list = [[dict_noms[i][1], dict_noms[i][0], j[1]] for i, j in dict_admin.items() if i in dict_noms.keys()]
    print(list)

    with open("out.csv", "w", newline="") as f:
        f_write = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in list:
            f_write.writerow(i)