from random import randint

A = []
B = []

for lista in range(10):
    lista = []

    for coluna in range(10):
        lista.append(randint(0, 100))
       
    A.append(lista)
    B.append(lista)
    
for lista_matriz in A:
    print(lista_matriz)
    
print('\n')

for list1 in B:
        print(list1)
