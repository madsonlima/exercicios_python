#Escolhe um número aleatório e compara com o chute do usuário.
from random import choice, randint
from time import sleep #faz o programa aguardar alguns segundos

#computador = [1, 2, 3, 4, 5]
#computadorescolha = choice(l1)
computadorescolha = randint(1,5)
usuarioescolha = int(input('Pensei em um número de 1 a 5, adivinhe qual foi!\n'))

print('Processando...')
sleep(2)

if usuarioescolha == computadorescolha:
    print('Você acertou!')
else:
    print('Você errou, era {}.'.format(n1))

#Lê a velocidade de um carro. Multa de 7 reais por km/h acima de 80km/h.
velocidade = float(input('A velocidade em que o carro estava:\n'))
if velocidade <= 80:
    print('Você não foi multado.')
else:
    multa = (velocidade-80)*7
    print('Você pagará uma multa de R${.2f}.'.format(multa))

#Diz se o número digitado é par ou ímpar.
n = int(input('Digite um número inteiro:\n'))
if n%2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')

#Calcula o preço da viagem por km, 0.5 para até 200km e 0.45 a partir de 200km.
quilometro = float(input('De quantos Km será a viagem?\n'))
#preco = quilometro * 0.5 if quilometro <= 200 else quilometro * 0.45
if quilometro <= 200:
    preco = quilometro*0.5
else:
    preco = quilometro*0.45
print('O preço será R${}.'.format(preco))

#Calcula se o ano é bissexto.
from datetime import date

ano = int(input('Qual ano deseja analisar como bissexto? (Digite 0 para analisar o ano atual.)\n'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))

#Lê 3 números, diz qual é o maior e o menor.
lista = []
lista.append(int(input('Digite o primeiro número: ')))
lista.append(int(input('Digite o segundo número: ')))
lista.append(int(input('Digite o terceiro número: ')))

lista = sorted(lista)
print('O menor número é {} e o maior é {}.'.format(lista[0], lista[2]))

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

menor = a
maior = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número é {} e o maior é {}.'.format(menor, maior))

#Calcula aumento de salário de 10% para superiores a 1250 e de 15% para inferiores ou iguais.
salario = float(input('Digite o salário: R$'))
if salario > 1250:
    print('O novo salário é R${}.'.format(salario*1.1))
else:
    print('O novo salário é R${}.'.format(salario*1.15))

#Lê o comprimento de 3 retas e diz se podem ou não formar um triângulo
n1 = float(input('Comprimento da primeira reta: '))
n2 = float(input('Comprimento da segunda reta: '))
n3 = float(input('Comprimento da terceira reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo.')
