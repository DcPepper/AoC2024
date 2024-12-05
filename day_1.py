from utils import parse_date

# Part - 1

data = parse_date(1)
liste_1 = []
liste_2 = []
for line in data:
    new_ints = [int(e) for e in line.split(' ') if e.isnumeric()]
    liste_1.append(new_ints[0])
    liste_2.append(new_ints[1])

liste_2.sort()
liste_1.sort()

print(sum([abs(x-y) for (x,y) in zip(liste_1, liste_2)]))

# Part - 2

liste_3 = []
for elt in liste_1:
    liste_3.append(elt * liste_2.count(elt))

print(sum(liste_3))


