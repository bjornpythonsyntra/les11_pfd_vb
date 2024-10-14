steden = ("Hasselt","Genk","As","Bree","Lommel")
for stad in steden:
    print(stad)
#hoe een element toevoegen aan een tuple?
print(steden)
steden = list(steden)
steden.append("Hoeselt")
steden = tuple(steden)
print(steden)
print(steden[:-3])
steden = list(steden)
steden.remove("As")
steden = tuple(steden)
print(steden)

