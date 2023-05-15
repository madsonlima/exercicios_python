#Lê um valor de sexo M ou F, se errado pede pra digitar novamente
sexo = str(input('Digite o sexo [M/F]: '))
while sexo not in 'MmFf':
    print('Sexo inválido. Digite novamente.')
    sexo = str(input('Digite o sexo [M/F]: '))
print('Sexo armazenado com sucesso!')

#Computador pensa em um número entre 1 e 5 e o jogador tenta adivinhar qual foi. Enquanto não adivinhar, o jogo continua.
from random import randint

numcomputador = randint(1,5)
numjogador = int(input('Jogo da advinha!\nAdvinhe o número que eu pensei: '))
tentativa = 1

while numjogador != numcomputador:
    numjogador = int(input('Você errou! Tente novamente: '))
    tentativa += 1

print('Você acertou! Era {}, você acertou em {} tentativas.'.format(numcomputador, tentativa))

#Lê dois valores e testa um menu com soma, multiplicação, maior/menor, novos valores e sair do programa.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
operacao = int(input('Digite o número de uma operação:\n'
                         '[1] Somar\n'
                         '[2] Multiplicar\n'
                         '[3] Maior valor\n'
                         '[4] Digitar novos valores\n'
                         '[5] Sair do programa\n'))
while operacao != 5:
    if operacao == 1:
        print('{} + {} = {}'.format(num1, num2, num1+num2))
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        operacao = int(input('Digite o número de uma operação:\n'
                             '[1] Somar\n'
                             '[2] Multiplicar\n'
                             '[3] Maior valor\n'
                             '[4] Digitar novos valores\n'
                             '[5] Sair do programa\n'))
    if operacao == 2:
        print('{} x {} = {}'.format(num1, num2, num1*num2))
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        operacao = int(input('Digite o número de uma operação:\n'
                             '[1] Somar\n'
                             '[2] Multiplicar\n'
                             '[3] Maior valor\n'
                             '[4] Digitar novos valores\n'
                             '[5] Sair do programa\n'))
    if operacao == 3:
        if num1 > num2:
            print('{} é maior que {}.'.format(num1, num2))
        if num2 > num1:
            print('{} é maior que {}.'.format(num2, num1))
        else:
            print('{} e {} são iguais.')
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        operacao = int(input('Digite o número de uma operação:\n'
                             '[1] Somar\n'
                             '[2] Multiplicar\n'
                             '[3] Maior valor\n'
                             '[4] Digitar novos valores\n'
                             '[5] Sair do programa\n'))
    if operacao == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        operacao = int(input('Digite o número de uma operação:\n'
                             '[1] Somar\n'
                             '[2] Multiplicar\n'
                             '[3] Maior valor\n'
                             '[4] Digitar novos valores\n'
                             '[5] Sair do programa\n'))
print('Programa encerrado.')

#Calcular o fatorial
numfixo = numero = int(input('Digite um número para verificar seu fatorial: '))
fatorial = 1

while numero != 1:
    fatorial = fatorial * numero
    numero -=1

print('{}! é {}.'.format(numfixo, fatorial))

#Progressão aritimética
primeiro = int(input('Progressão Aritmética! (10 primeiros números)\nDigite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao #fórmula para descobrir o x termo de uma PA
while primeiro != decimo+razao:
    print(' {} '.format(primeiro),end='')
    primeiro += razao

#Progressão aritmética perguntando se quer mortrar mais termos
primeiro = int(input('Progressão Aritmética!\nDigite o primeiro termo: '))
razao = int(input('Digite a razão: '))
xnum = 10
while xnum != 0:
    decimo = primeiro + (xnum - 1) * razao  # fórmula para descobrir o x termo de uma PA
    while primeiro != decimo + razao:
        print(' {} '.format(primeiro), end='')
        primeiro += razao
    xnum = int(input('\nQuantas mais posições você quer ver? (Digite 0 para sair)\n'))
print('Programa encerrado')

#Sequência de Fibonacci
num = int(input('Digite um número para iniciar a Sequência de Fibonacci a partir dele: '))
opt = int(input('Quantos elementos da sequência deseja mostrar? '))

cont = 1
numanterior = num - 1
proximo = num + numanterior
print('{} - \033[31m{}\033[m - '.format(numanterior, num),end='')
while cont != opt+1:
    print('{} - '.format(proximo),end='')
    numanterior = num
    num = proximo
    proximo = num + numanterior
    cont += 1
print('FIM')

#Lê vários números até ser digitado 999, então soma todos eles
soma = num = int(input('SOMA DE NÚMEROS\nDigite um número:\n'))
cont = 1
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite outro número (digite 999 para parar):\n'))
print('Você digitou {} valores, e a soma deles é {}.'.format(cont,soma))

#Lê números inteiros, faz a média entre eles e diz qual foi o maior e o menor valor. No final pergunta se quer continuar a digitar.
num = int(input('Digite um número: '))

menor = maior = num
soma = cont = 0
continuar = 'S'

while continuar in 'S':
    soma += num
    cont += 1

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    continuar = str(input('Deseja continuar? [s/n] ')).upper().strip()[0] #coloca a str em maiusculas e pega so o primeiro caractere
    if continuar in 'S':
        num = int(input('Digite outro número: '))
print('{} números foram digitados, a média é {}, o maior número digitado foi {} e o menor foi {}.'.format(cont, (soma)/(cont), maior, menor))

#Tabuada de vários números de cada vez, parando quando um valor negativo for inserido
print('Digite um número negativo para sair.')
while True:
    num = int(input('Tabuada do número: '))
    if num < 0:
        break
    print('TABUADA DO {}'.format(num))
    for aux in range(1,11):
        print('{} * {} = {}'.format(num, aux, num*aux))
print('FIM')

#Par ou ímpar. Só para quando o jogador perder
from random import randint
vitoria = 0
while True:
    opcao = str(input('====================\nPAR OU ÍMPAR? ')).upper().strip()[1]
    num = int(input('Digite um número: '))
    numpc = randint(0, 9)
    print(f'Computador: {numpc}')
    final = num + numpc

    if final%2 == 0:
        if opcao == 'A':
            print('Você acertou!')
            vitoria += 1
        elif opcao == 'M':
            print('Você errou...')
            break
    else:
        if opcao == 'A':
            print('Você errou...')
            break
        elif opcao == 'M':
            print('Você acertou!')
            vitoria += 1
print(f'FIM! Você acertou {vitoria} vezes.')

#Lê idade e sexo de várias pessoas e pergunta se quer continuar. No final diz quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem mais de 20 anos.
aux = idadesoma = dezoito = homens = mulheres = 0
sexo = '0'
flag = 1
while True:
    aux += 1
    idade = int(input('====================\nPessoa {}\nIdade: '.format(aux)))
    while sexo != 'M' and sexo != 'F': #while sexo not in 'MF':
        sexo = str(input('Sexo: (M/F) ')).upper()

    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade > 20:
        mulheres += 1

    sexo = '0'
    flag = str(input('Quer continuar? (S/N) ')).upper()
    if flag == 'N':
        break
print('Concluído.\n{} pessoas são maiores de idade.\n{} homens foram cadastrados.\n{} mulheres cadastradas tem mais de 20 anos.'.format(dezoito,homens,mulheres))

#Lê o nome dos produtos e o preço. No final mosta o total gasto na compra, quantos produtos custam mais de 1000 e qual o nome do produto mais barato
aux = total = mil = 0
while True:
    aux += 1
    continuar = '0'
    print('========== PRODUTO {} =========='.format(aux))
    nome = str(input('Nome: '))
    preco = float(input('Preço: R$'))

    total += preco
    if preco > 1000:
        mil += 1
    if aux == 1:
        menorn = nome
        menorp = preco
    elif preco < menorp:
        menorn = nome
        menorp = preco

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? (S/N) ')).upper()
    if continuar == 'N': #tem que ser fora do segundo while!
        break

print(f'Total gasto: R${total}\n'
      f'{mil} produtos custam mais de R$1000.\n'
      f'O produto mais barato é {menorn}, que custa R${menorp}.')

#Simular um caixa eletrônico, que pergunta o valor a ser sacado e o programa indica quantas cédulas de cada valor (50, 20, 10, 1) serão entregues
print('SAQUE DO CAIXA')
saque = int(input('Quanto deseja sacar? R$ '))
aux = 0
cinquenta = vinte = dez = um = 0

while aux != saque:
    if (aux + 50) <= saque:
        aux += 50
        cinquenta += 1
    elif (aux + 20) <= saque:
        aux += 20
        vinte += 1
    elif (aux + 10) <= saque:
        aux += 10
        dez += 1
    elif (aux + 1) <= saque:
        aux += 1
        um += 1

print(f'Saque:\n'
      f'{cinquenta} notas de R$50,00\n'
      f'{vinte} notas de R$20,00\n'
      f'{dez} notas de R$10,00\n'
      f'{um} notas de R$1,00')