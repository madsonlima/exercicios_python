#Empréstimo bancário. Pergunta o valor da casa, o salário e em quantos anos vai pagar. A prestação não pode ser mais de 30% do salário.
print('Financiamento')
casa = float(input('Qual o valor da casa visada? R$'))
sala = float(input('Qual seu salário atual? R$'))
anos = int(input('Em quantos anos deseja parcelar?'))

parcela = casa/(12*anos)
if parcela > (sala*0.3):
    print('O financiamento está disponível. A parcela mensal em {} anos será R${}.'.format(anos,parcela))
else:
    print('O financiamento não está disponível.')

#Conversor de Bases Numéricas. Converter número inteiro para binário, octal ou hexadecimal.
num = int(input('Digite um número inteiro: '))
opt = int(input('Converter para:\n'
                '[1]Binário\n'
                '[2]Octal\n'
                '[3]Hexadecimal\n'))

if opt == 1:
    print('{} em binário é {}.'.format(num,bin(num)[2:]))
elif opt == 2:
    print('{} em octal é {}.'.format(num,oct(num)[2:]))
elif opt == 3:
    print('{} em hexadecimal é {}.'.format(num,hex(num)[2:]))
else:
    print('Digite uma opção válida.')

#Compara números, maior, menor ou igual.
print('Comparador de números')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2:
    print('{} é maior que {}!'.format(n1,n2))
elif n1 < n2:
    print('{} é maior que {}!'.format(n2,n1))
else:
    print('Os números são iguais!')

#Calculo de alistamento militar.
from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year-ano
print('Você completará {} anos este ano.'.format(idade))
if idade == 18:
    print('Você deverá se apresentar este ano.')
elif idade < 18:
    print('Seu alistamento ainda não está disponível, espere mais {} anos, até {}.'.format(18-idade, date.today().year+(18-idade)))
else:
    print('Você deveria ter se apresentado a {} anos atrás, em {}!'.format(idade-18, date.today().year-(idade-18)))

#Cálculo de média
from datetime import date
n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a note da segunda prova: '))
n3 = float(input('Digite a nota da terceita prova: '))
media = (n1+n2+n3)/3
if media >= 7:
    print('Você foi aprovado!')
elif media > 5:
    print('Você está de recuperação!')
else:
    print('Você foi reprovado!')

#Classificação de atletas nadadores
ano = int(input('Classificação de nadadores.\nEm que ano a pessoa nasceu? '))
idade = date.today().year-ano
if idade <= 9:
    print('Nadador mirim.')
elif idade <= 14:
    print('Nadador infantil.')
elif idade <= 19:
    print('Nadador júnior.')
elif idade <= 25:
    print('Nadador sênior.')
else:
    print('Nadador master.')

#Classificação de triângulos
n1 = float(input('Comprimento da primeira reta: '))
n2 = float(input('Comprimento da segunda reta: '))
n3 = float(input('Comprimento da terceira reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print('É um triângulo equilátero.')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('É um triângulo isóceles.')
    else:
        print('É um triângulo escaleno.')
else:
    print('As retas não podem formar um triângulo.')

#Índice de massa corporal
print('Cálculo de IDM (índice de massa corporal)')
peso = float(input('Digite seu peso (kg): '))
altu = float(input('Digite sua altura (m): '))
idm = peso/(altu**2)
if idm < 18.5:
    print('Você está abaixo do peso ideal.')
elif idm <= 25:
    print('Seu peso é ideal.')
elif idm <= 30:
    print('Você está com sobrepeso.')
elif idm <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')

#Descontos por pagamento
valor = float(input('Digite o valor total das compras: R$'))
opt = int(input('Escolha o método de pagamento:\n'
                '[1] à vista dinheiro/cheque\n'
                '[2] à vista no cartão\n'
                '[3] em até 2x no cartão\n'
                '[4] 3x ou mais no cartão\n'))
if opt == 1:
    print('O valor final das compras será de R${}.'.format(valor*0.9))
elif opt == 2:
    print('O valor final das compras será de R${}.'.format(valor*0.95))
elif opt == 3:
    print('O valor final das compras continuará o mesmo, R${} em duas parcelas de R${}.'.format(valor,valor/2))
elif opt == 4:
    parcelas = int(input('Em quantas parcelas deseja pagar? '))
    print('O valor final das compras será de R${}, em {} parcelas de R${}.'.format(valor*1.2,parcelas,(valor*1.2)/parcelas))
else:
    print('Opção inválida de pagamento.')

#Pedra, papel, tesoura
from random import randint
from time import sleep
print('PEDRA, PAPEL, TESOURA!')
jogador = int(input('Qual a sua jogada?\n'
                '[1] PEDRA\n'
                '[2] PAPEL\n'
                '[3] TESOURA\n'))
computador = randint(1,3)

print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.5)
print('TE-')
sleep(0.3)
print('SOURA!')

if jogador == 1:
    if computador == 1:
        print('Jogador jogou PEDRA')
        print('Computador jogou PEDRA')
        sleep(0.5)
        print('EMPATE!')
    elif computador == 2:
        print('Jogador jogou PEDRA')
        print('Computador jogou PAPEL')
        sleep(0.5)
        print('COMPUTADOR VENCEU!')
    elif computador == 3:
        print('Jogador jogou PEDRA')
        print('Computador jogou TESOURA')
        sleep(0.5)
        print('JOGADOR VENCEU!')
elif jogador == 2:
    if computador == 1:
        print('Jogador jogou PAPEL')
        print('Computador jogou PEDRA')
        sleep(0.5)
        print('JOGADOR GANHOU!')
    elif computador == 2:
        print('Jogador jogou PAPEL')
        print('Computador jogou PAPEL')
        sleep(0.5)
        print('EMPATE!')
    elif computador == 3:
        print('Jogador jogou PAPEL')
        print('Computador jogou TESOURA')
        sleep(0.5)
        print('COMPUTADOR VENCEU!')
elif jogador == 3:
    if computador == 1:
        print('Jogador jogou TESOURA')
        print('Computador jogou PEDRA')
        sleep(0.5)
        print('COMPUTADOR GANHOU!')
    elif computador == 2:
        print('Jogador jogou TESOURA')
        print('Computador jogou PAPEL')
        sleep(0.5)
        print('JOGADOR GANHOU!')
    elif computador == 3:
        print('Jogador jogou TESOURA')
        print('Computador jogou TESOURA')
        sleep(0.5)
        print('EMPATE!')
else:
    print('Jogada inválida.')