from functools import reduce

# q1
triple = lambda x: 3 * x
print(triple(3))

# q2

est_pair = lambda x: x % 2 == 0
print(est_pair(4))


# q3

def multiplicateur(n):
    return lambda x: x * n


print(multiplicateur(5)(3))

# q4

l = [i for i in range(10) if i % 2 != 0]
print(l)

# q5

l1 = [i * 3 for i in range(1, 11)]
print(l1)

l2 = []
for i in list(range(1, 11)):
    i = i * 3
    l2.append(i)
print(l2)

# q6

l1 = list(map(lambda x: x * 3, filter(lambda x: x % 2 == 0, range(1, 11))))
print(l1)

l2 = [i * 3 for i in range(1, 11) if (i * 3) % 2 == 0]
print(l2)

# q7

produit = lambda x, y: x * y
print(reduce(produit, range(1, 11)))

# q8

factorielle = lambda x: reduce(lambda x, y: x * y, range(1, x + 1), 1)
print(factorielle(5))

# q9

list = ["a", "b", "c"]
print("_".join(list))

# q10

list = [1, 4, 3, 7]
dict = {i: i % 2 == 0 for i in list}
print(dict)

# q11

def indent(x):
    return f"{x[1]}:\n{x[0]};\t{x[2]}!"

print(indent([1,2,3]))

# q12

def extraire_longs_mots(x):
    list = ";".join(sorted(filter(lambda x: len(x) > 3, map(str.lower, x.split()))))
    return list

print(extraire_longs_mots("Ich heisse Yannic alte"))



# avance

# q1

def lister_int(n):
    list = []
    while n > 0:
        list.append(n)
        n -= 1
    list = sorted(list)
    list = ",".join(map(str, list))
    return list

print(lister_int(10))

# q2

l1 = ["Albert Troussard", "Elias Amine", "Imane Jennane", "Mathieu Faure", "Valentin Parisot"]
l2 = ["EPFL", "UNIL", "EPFL", "EPFL", "EPFL"]

list = ",".join([i for i, j in zip(l1, l2) if j == "UNIL"])

print(list)

# q3

l = [[2, 3, 4], [1], [2, 7]]
l1 = ["".join(map(str, y)) for y in l]
x = "/".join(l1)

print(x)

# q4

def covertir_noms(x):
    if len(x) > 2:
       formated = " ". join(f"{name[0]}." for name in x[1:-1])
       return f"{x[0]} {formated} {x[-1]}"
    else:
        return " ".join(x)

print(covertir_noms(["John", "Peters", "Müller"]))

# q5

infractions = [
    ("Edward", "Elric", 5),
    ("Izumi", "Curtis", 9),
    ("King", "Bradley", 0),
    ("Maes", "Hughes", 4)
]

infractions.sort(key=lambda x: x[2], reverse=True)

print(infractions)

# q6

d = {"fruit": "banane", "legume": "carotte"}

d = {v:k for k,v in d.items()}

print(d)

# q7

d1 = {3: "voiture", 2: "velo"}
d2 = {3: "rouge", 1: "bleu"}
l = []

for i in d1.keys():
    for j in d2.keys():
        if i == j:
            l.append((d1[i], d2[j]))

print(l)

# q8

l = ["Josephine Meyer", "Max Weber", "Noah Wagner", "Liam Wagner", "Liam Fischer", "Simona Schmidt"]
l = map(lambda x: x.lower(), l)

for i in l:
    x = f"{i.replace(' ', '.')}@unil.ch"
    print(x)

