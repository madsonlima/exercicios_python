#Ler 5 valores, e mostrar qual o maior e menos e a posição deles
valores = list()
maiorpos = []
menorpos = []

for aux in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if aux == 0:                        #para reconhecer o primeiro menor e maior
        maior = menor = valores[aux]
    else:
        if valores[aux] > maior:        #para armazenar o maior e menor
            maior = valores[aux]
        elif valores[aux] < menor:
            menor = valores[aux]

for pos, val in enumerate(valores):     #para varrer a lista, comparar e armazenar as posições
    if val == maior:
        maiorpos.append(pos)
    if val == menor:
        menorpos.append(pos)

print(f'O maior número digitado foi {maior} nas posições {maiorpos}.\n'
      f'O menor número digitado foi {menor} na posições {menorpos}.')

#Recebe números para armazenar em uma lista, que não podem ser repetidos, e quando pedir para parar, mostrar em ordem crescente
num = list()
continuar = 's'
while continuar in 'simSIM':
    numaux = int(input('Digite um número: '))
    if numaux in num:
        print('Valor duplicado não adcionado. ==')
    else:
        num.append(numaux)
        print('Valor adcionado. ++')
    continuar = str(input('Deseja continuar? [S/N] '))

num.sort(reverse=True)      #organiza em reverso

print(f'Programa encerrado.\n'
      f'Ordem crescente: {sorted(num)}\n'   #printa organizado
      f'Ordem decrescente: {num}.')

#Cria uma lista que recebe numeros e automaticamente já organiza, sem usar sort()
listanum = list()
for aux in range(0,5):
    auxnum = int(input(f'{aux+1}° número: '))
    if aux == 0 or auxnum > listanum[len(listanum)-1]:
        listanum.append(auxnum)
    elif auxnum < listanum[0]:
        listanum.insert(0,auxnum)
print('Organizado: ',listanum)

#Lê vários números e mostra: quantos num, lista ordenada, e se existe 5 ou não
valornum = list()
continuar = 's'
while continuar in 'simSIM':
    valornum.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] '))

print(f'Você digitou {len(valornum)} números\n'
      f'Organizado: {sorted(valornum)}\n'
      f'O valor 5 apareceu {valornum.count(5)} vezes.')

#Lê números e coloca e uma lista, depois mostra a lista e mais duas para os pares e impares
listainteira = list()
listapar = list()
listaimpar = list()
auxnum = 0
continuar = 's'
while continuar in 'simSIM':
    auxnum = int(input('Digite um número: '))
    listainteira.append(auxnum)
    if auxnum % 2 == 0:
        listapar.append(auxnum)
    else:
        listaimpar.append(auxnum)
    continuar = str(input('Quer continuar? [S/N] '))
print(f'Lista inteira: {listainteira}\n'
      f'Lista de pares: {listapar}\n'
      f'Lista de ímpares: {listaimpar}')

#Verifica es a expressão está válida em relação a abertura e fechamento de parênteses
expressao = str(input('Expressão: '))
if expressao.count('(') == expressao.count(')'):
    print('A expressão é válida.')
elif:
    print('A expressão não é válida.')

#Lê nome e peso de pessoas em listas, diz quantas pessoas foram cadastradas, lista com as pessoas mais pesadas e outra com as mais leves
pessoas = list()
pessoasaux = list()
pesados = list()
leves = list()
maior = menor = 0
continuar = 's'

while continuar in 'simSIM':
    pessoasaux.append(str(input('Nome: ')))
    pessoasaux.append((float(input('Peso: '))))     #lista de auxilio

    if len(pessoas) == 0:
        maior = menor = pessoasaux[1]
    else:
        if pessoasaux[1] > maior:
            maior = pessoasaux[1]
        if pessoasaux[1] < menor:
            menor = pessoasaux[1]

    pessoas.append(pessoasaux[:])                   #lista principal recebe a de auxilio
    pessoasaux.clear()                              #lista de auxilio é limpa
    continuar = str(input('Continuar? [S/N] '))

for p in pessoas:
    if p[1] == maior:
        pesados.append(p[0])
    if p[1] == menor:
        leves.append(p[0])

print(f'{len(pessoas)} pessoas foram cadastradas.')
print(f'O maior peso foi {maior} de {pesados}\n'
      f'O menor peso foi {menor} de {leves}')

#receber numeros e manter separados dentro dessa lista por par e impar
numeros = [[], []]
auxiliar = 0

for aux in range(0, 3):
    auxiliar = int(input(f'{aux+1}° número: '))
    if auxiliar % 2 == 0:
        numeros[0].append(auxiliar)
    else:
        numeros[1].append(auxiliar)

numeros[0].sort()
print(f'Pares: {numeros[0]}\n'
      f'Ímpares: {sorted(numeros[1])}')

#Ler uma matriz de 3x3 e mostrar na formatação correta
matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]

for aux in range(0, 3):
    for ili in range(0, 3):
        matriz[aux][ili] = int(input(f'Linha {aux+1}, coluna {ili+1}: '))
for aux in range(0, 3):
    for ili in range(0, 3):
        print(f'[{matriz[aux][ili]:^5}]',end='')
    print()

#Exercício anterior, agora mostrando: soma dos valores pares, soma dos valores da terceira coluna e o maior valor da segunda linha.
matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
pares = 0
coltres = 0
maior = 0

for aux in range(0, 3):
    for ili in range(0, 3):
        matriz[aux][ili] = int(input(f'Linha {aux+1}, coluna {ili+1}: '))
        if matriz[aux][ili] % 2 == 0:           #soma dos pares
            pares += matriz[aux][ili]
        if ili == 2:                            #soma da terceira coluna
            coltres += matriz[aux][ili]

for aux in range(0, 3):                         #verificação do maior na segunda linha
    if aux == 0:
        maior = matriz[1][aux]
    else:
        if matriz[1][aux] > maior:
            maior = matriz[1][aux]

for aux in range(0, 3):
    for ili in range(0, 3):
        print(f'[{matriz[aux][ili]:^5}]',end='')
    print()

print(f'Soma dos pares: {pares}\n'
      f'Soma da terceira coluna: {coltres}\n'
      f'Maior da segunda linha: {maior}')

#Perguntar quantos jogos serão gerados e sortear 6 numeros de 1 a 60 para cada jogo, armazenados em uma lista composta
from random import randint
from time import sleep
jogos = list()
recebendo = list()
sorteado = 0

quant = int(input('Sortear quantos jogos? '))
for aux in range(0, quant):
    while True:
        if len(recebendo) == 6:
            break
        sorteado = randint(1, 60)
        if sorteado not in recebendo:
            recebendo.append(sorteado)
    recebendo.sort()
    jogos.append(recebendo[:])
    recebendo.clear()

for aux, ili in enumerate(jogos):
    sleep(0.5)
    print(f'{aux+1}° jogo: {ili}')
print('Boa sorte!')

#Le alunos e 2 notas de cada, no final mostra formatado cada aluno com sua média. Se escolher um aluno será mostrado suas notas
listaluno = list()
listnotas = list()
listmedia = list()
auxaluno = list()
auxnotas = list()
media = 0
continuar = 's'
cont = 0
verificar = 0
while continuar in 'simSIM':
    auxaluno.append(str(input('Nome: ')))
    for aux in range(0, 2):
        auxnotas.append(float(input(f'Nota {aux+1}: ')))

    listaluno.append(auxaluno[:])
    listnotas.append(auxnotas[:])
    auxaluno.clear()
    auxnotas.clear()

    cont += 1
    continuar = str(input('Continuar? [S/N] '))

for aux in range(0, cont):
    for ili in range(0, 2):
        media += listnotas[aux][ili]
    listmedia.append(media/2)
    media = 0

for aux in range(0, cont):
    print(f'{aux:^3}',end='')
    print(f'{listaluno[aux]}',end='')
    print(f'{listmedia[aux]}')

while True:
    verificar = int(input('Verificar as notas de que aluno? [999 encerra] '))
    if verificar == 999:
        break
    print(f'Aluno: {listaluno[verificar]}\n'
          f'Notas: {listnotas[verificar]}')

print('Fim do programa.')

#Mesmo programa anterior feito de forma mais simples
ficha = list()
continuar = 's'
verificar = 0

while continuar in 'simSIM':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input('Continuar? [S/N] '))

print('=' * 30)
print(f'{"ID":^6} {"NOME":^14} {"MÉDIA":^8}')
print('=' * 30)
for aux in range(0, len(ficha)):
    print(f'{aux:^6} {ficha[aux][0]:^14} {ficha[aux][2]:^8}')
'''
for pos, val in enumerate(ficha):
    print(f'{pos:^6} {ficha[val][0]:^14} {ficha[val][2]:^8}')
'''
print('=' * 30)

while True:
    verificar = int(input('Verificar notas por ID: [Parar: 999] '))
    if verificar == 999:
        break
    if verificar >= 0 and verificar <= len(verificar) - 1:
        print(f'Aluno: {ficha[verificar][0]}\n'
              f'Nota 1: {ficha[verificar][1][0]} | Nota 2: {ficha[verificar][1][1]}')
        print('=' * 30)

print(f'{"\nPROGRAMA ENCERRADO":^30}')
