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
