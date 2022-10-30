import random

matriz = [[], [], [], [], [], [], [], [], [], []]

for b in range(0,10):
    num = random.randint(0, 100)
    matriz[b].append(num)
    for c in range(0, 10):
        matriz[c].append(num)

for b in range(0, 10):
    for c in range(0, 10):
        print(f'[{matriz[b][c]:^5}]', end='')
    print()
