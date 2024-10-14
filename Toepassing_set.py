import random

# De vijf steden
steden = ["Hasselt", "Genk", "Bree", "As", "Bilzen"]

# Een lijst met 24 willekeurige steden
willekeurige_steden = [random.choice(steden) for _ in range(24)]

print(willekeurige_steden)
locaties = set(willekeurige_steden)
locaties = list(locaties)
print(locaties)
