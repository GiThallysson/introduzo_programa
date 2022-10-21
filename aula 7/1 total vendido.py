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
