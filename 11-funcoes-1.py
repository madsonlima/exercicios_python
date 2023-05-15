#Criar função pra criar uma linha de caracteres.
def mostraTitulo(titulo):    # parâmetro
    print('-' * 30)
    print(f'{titulo:^30}')
    print('-' * 30)
#Programa principal
mostraTitulo('Madson')       # parâmetro = 'Madson'

#Criar função pra somar numeros e mostrar
def soma(x, y):
    s = x + y
    print(s)
soma(y=2, x=2)

#--------------------------------------------------
mostraTitulo('Empacotamento')

def contador(* num):    #Número de parâmetros indefinido. Armazena em uma tupla.
    print(num)          #Mostra a tupla com todos os parâmetros.
    s = 0
    for valor in num:
        s += valor                     #Soma
        print(f'{valor} ', end='')
    print()
    print('Quantidade:', len(num))     #Mostra a quantidade de valores da tupla.
    print(f'Soma: {s}')                #Mostra a soma
contador(1, 2, 3, 4, 5)

#--------------------------------------------------
mostraTitulo('Função com listas')

def dobra(lista):
    pos = 0
    while pos < len(lista):     #Vai interferir diretamente em valores!
        lista[pos] *= 2
        pos += 1

valores = [1, 2, 3, 4, 5]
print(valores)
dobra(valores)      #Vai interferir diretamente em valores!
print(valores)

#--------------------------------------------------
mostraTitulo('Área de um terreno')
def area(cmp,lrg):
    n3 = cmp * lrg
    print(f'Área: {n3}m²')
n1 = float(input('Comprimento: (m) '))
n2 = float(input('Largura: (m) '))
area(n1, n2)

#--------------------------------------------------
mostraTitulo('Título adaptável')
def Titulo(tit):
    tamanho = len(tit) + 6
    print('-' * tamanho)
    print(f'   {tit}')
    print('-' * tamanho)
Titulo('Título adaptável')

#--------------------------------------------------
Titulo('Contador')
from time import sleep
def Contador(ini,fim,passo):
    print(f'Contagem de {ini} a {fim}, de {passo} em {passo}:')
    if fim > ini:
        for aux in range(ini,fim+1,passo):
            print(f'{aux} ',end='')
            sleep(0.5)
        print('Fim!')
    else:
        if passo > 0:
            passo = passo - (passo * 2)     #Se tiver positivo, transforma pra negativo
        for aux in range(ini, fim-1, passo):
            print(f'{aux} ', end='')        #, flush=True (desliga o buffer de tela, caso a contagem aguarde os
            sleep(0.5)                      #segundos pra mostrar inteira ao invés de uma por uma a cada 0.5 segundos.)
        print('Fim!')
    print('~' * 30)
Contador(1,10,1)
Contador(10,1,2)
Contador(10,1,-1)
print(f'Sua vez!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
Contador(ini,fim,passo)

#--------------------------------------------------
Titulo('Descobrir o maior')

def MostraMaior(num):
    print(num)
    maior = num[0]
    for valor in num:
        if valor > maior:
            maior = valor
    print('Maior: ',maior)
MostraMaior([3, 1, 6, 9, 0])

print('Digite números para descobrir o maior: ')
continuar = 1
maiorusuario = list()
while continuar > 0:
    maiorusuario.append(int(input('Número: ')))
    continuar = int(input('Continuar? [1 = Sim][0 = Não] '))
MostraMaior(maiorusuario)

#--------------------------------------------------
Titulo('Função para sortear números e somar os pares')

from random import randint
from time import sleep
def Sortear(lista):
    for aux in range(0, 5):
        lista.append(randint(0,9))

def SomaPar(lista):
    soma = 0
    for aux in lista:
        if aux % 2 == 0:
            soma += aux
    print(f'Soma dos pares: {soma}')

numeros = list()        # Para retornar a lista preenchida, uma lista vazia deve ser criada antes de iniciar a função.
Sortear(numeros)        # Aqui a função vai adicionar números aleatórios a ela.

for aux in numeros:
    print(aux,end=' ')
    sleep(0.5)
print()
SomaPar(numeros)        # O print está dentro da função.
