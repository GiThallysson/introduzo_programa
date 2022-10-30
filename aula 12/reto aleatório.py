import random

matriz = [[], [], []]

for b in range(0,3):
    num = random.randint(0, 100)
    matriz[b].append(num)
    for c in range(0, 3):
        matriz[c].append(num)

for b in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[b][c]:^5}]', end='')
    print()
