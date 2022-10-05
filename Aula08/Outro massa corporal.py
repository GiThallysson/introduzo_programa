# 01 - [FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), 
# sendo que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raizes reais).
 
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))

d = (b**2) - (4*a*c) 

x1 = (-b-d)/(2*a) 
x2 = (-b+d)/(2*a)

print(f"X1: {x1} e x2: {x2}")




# 2 -[FORBELLONE, 2022] Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano, P(x1, y1) e Q(x2, y2), imprima a distância entre eles. A formulá que efetua tal cálculo é: d = (x2 - x1)² + (y2 - y1)²

x1 = int(input("Digite uma valor para x1: "))
x2 = int(input("Digite uma valor para x2: "))
y1 = int(input("Digite uma valor para y1: "))
y2 = int(input("Digite uma valor para y2: ")) 

d = ((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**(0.5) 

print(f"A distância entre os pontos é {d}")

#3. Elabore um algoritmo que leia o valor de dois números inteiros e a operacão aritimética desejada; calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual operacão
#aritmética escolhida.
Símbolo
+
-
*
/ 
**

Operação aritmética
Adição
Subtração
Multiplicacão
Divisão
Potenciação

n1 = int(input('digite um número '))
n2 = int(input('digite próximo número '))
r = input('qual operação deseja fazer')
if r == "+":
    s = n1+n2 
    print(s)
elif r == "-":
    s = n1-n2
    print(s)
elif r == "*":
    s = n1*n2
    print(s)
elif r == "/":
    s = n1/n2
    print(s)
elif r == "**":
    s = n1**n2
    print(s)
else:
    print('faz o novo')

#4. O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar a
#condição de peso de uma pessoa. A fórmula é IMC= peso / (altura). Elabore um algoritmo que leia o
#peso e a altura de uma adulto e mostre sua condição.

massa = float (input("qual seu peso em quilogramas"))
altura = float( input (" qual sua altura"))
imc= (massa/ (altura**2))
if imc < 18.5:
    print("abaixo do peso")
elif 18.5 <imc<24.9:
     print("peso normal")
elif 25<=imc<29.9:
     print("acima do peso" )
elif 30<=imc<34.9:
     print ("obeso ")
else:
       print ("você está na obesidade III Grau")


#5. Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar 
#quando for lido um número negativo.

n = 1
i = 0
i2 = 0
i3 = 0
i4 = 0

while n >= 0:
    n = int(input('digite um valor: '))
    if 0<n<25:
        i += 1
    elif 26<n<50:
        i2 += 1
    elif 51<n<75:
        i3 += 1
    elif 76<n<100:
        i4 += 1
    else:
        print


print(i)
print(i2)
print(i3)
print(i4)

#6. Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X4 X 3 X 2 X 1 = 120

from math import factorial
f = factorial (5)
print(f) 
