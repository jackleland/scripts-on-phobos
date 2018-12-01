import random


names = ['Tom', 'Sam W', 'Michail', 'James', 'Frederico']
desks = [4, 5, 7, 10, 11, 13]

choices = {}
for name in names:
    pick = random.randint(0, len(desks))
    choices[name] = desks[pick]
    desks.pop(pick)

print(choices)
