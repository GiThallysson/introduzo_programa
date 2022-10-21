'''
1. Escreva um algoritmo que permita a leitura dos nomes
   de 10 clubes de futebol e armazene os nomes lidos em
   um vetor (lista). Após isto, o algoritmo deve permitir
   a leitura de mais 1 nome qualquer de clube e depois
   escrever a mensagem ACHEI, se o nome estiver entre os
   10 nomes lidos anteriormente (guardados no vetor), ou
   NÃO ACHEI caso contrário.
'''

clubes = []

while True:
  clube = input("Clube que deseja armazenar: ")
  clubes.append(clube)

  if len(clubes) == 10:
    break

clube = input("Clube que deseja buscar: ")

if clube in clubes:
  print("ACHEI")
else:
  print("M ACHOU")

'''
2. Faça um algoritmo para ler um vetor de 30 números.
   Após isto, ler mais um número qualquer, calcular e
   escrever quantas vezes esse número aparece no vetor.
'''

vetor = []

while True:
  num = float(input("Digite um número: "))
  vetor.append(num)

  if len(vetor) == 30:
    break

x = float(input("Digite mais um número: "))
teve = 0

for num in vetor:
  if x == num:
    teve += 1

print(f"Ocorrências do número {x} no vetor o lista: {teve}")
