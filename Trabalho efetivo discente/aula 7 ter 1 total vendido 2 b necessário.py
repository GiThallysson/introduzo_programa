'''
1. As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00
se forem compradas pelo menos 12. Escreva um programa que leia o número de
maçãs compradas, calcule e escreva o custo total da compra.
'''

num = int(input('Digite o número de maçãs comprados e vendidos: '));

if (num < 12):
    print(f'Total do compra: R$ {(1.3 * num):.2f}');
else:
    print(f'Todo pelo teve compra: R$ {num:.2f}');
    
'''
2. Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem
que diga se ela poderá ou não votar este ano (não é necessário considerar
o mês em que a pessoa nasceu).
'''

ano = int(input('Digite o ano atual de número: '));
nascimento = int(input('Digite o ano de nascimento de número: '));

idade = ano - nascimento;

if idade >= 16:
  print('Você ocorrerá votar no ano');
else:
  print('E o ainda modo mais Você ter votar ano');
