from tabulate import tabulate

# De Lotto-trekkingen als lijst
lotto = [(5,18,21,27,33,37,42),(3,4,9,12,20,24,36)]
lotto_klas = {"Guven":(5,18,21,27,33,37,42),"Roberto":(3,4,9,12,20,24,36)}
print(lotto_klas["Guven"])

# Tabel maken
table = tabulate(lotto, headers=["Nummer 1", "Nummer 2", "Nummer 3", "Nummer 4", "Nummer 5", "Nummer 6", "Bonusnummer"], tablefmt="grid")

# Print de tabel
print(table)

