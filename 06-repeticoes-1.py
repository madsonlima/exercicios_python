#Contagem regressiva
from time import sleep

input('Pressione ENTER para iniciar!')
for aux in range(10,0,-1):
    print('{}! '.format(aux),end='')
    sleep(1)
print('FELIZ ANO NOVO!!!')

#Todos os números pares em um intervalo
print('Números pares em um intervalo de números.')
minimo = int(input('Digite o limite mínimo: '))
maximo = int(input('Digite o limite máximo: '))

if minimo%2 == 1:
    minimo = minimo+1 #confirma que o primeiro número vai ser sempre par

for minimo in range(minimo,maximo+1,2): #acrescenta o mínimo de dois em dois e imprime
    print('{}, '.format(minimo),end='')
print('fim.')

#Soma dos números ímpares múltiplos de 3
print('Soma dos números ímpares múltiplos de 3 entre 1 e 500:')
soma = 0
cont = 0
for aux in range(1,500+1):
    if aux%2 != 0:
        if aux%3 == 0:
            soma = soma+aux
            cont += 1
print('{}! {} números.'.format(soma, cont))

#Tabuada
tab = int(input('Tabuada!\nDigite um número: '))
for mult in range(1,11):
    print('{} x {} = {}'.format(tab,mult,tab*mult))

#Lê 6 números inteiros e faz a soma dos números pares inseridos
print('Soma dos números pares.')
soma = 0
for aux in range(0,6):
    num = int(input('Digite o {}° número: '.format(aux+1)))
    if num%2 == 0:
        soma = soma+num
print('A soma dos números pares é {}!'.format(soma))

#Progressão aritimética
primeiro = int(input('Progressão Aritmética! (10 primeiros números)\nDigite o primeiro termo: '))
razao = int(input('Digite a razão: '))
'''
for aux in range(0,10):
    print('{}, '.format(primeiro),end='')
    primeiro = primeiro + razao
print('fim.')
'''
decimo = primeiro + (10 - 1) * razao #fórmula para descobrir o x termo de uma PA
for primeiro in range(primeiro,decimo+razao,razao):
    print('{}, '.format(primeiro),end='')
print('fim.')

#Número primo
print('É ou não um número primo?')
num = int(input('Digite um número: '))
soma = 0
for aux in range(1,num+1):
    if num%aux == 0: #verifica se é divisível
        soma=soma+1
        print('{} {} {} '.format('\033[4;;40m',aux,'\033[m'),end='') #pinta o número divisível
    else:
        print('{} '.format(aux),end='')
if soma == 2: #se foi divisível só por 2 (1 e ele mesmo), então é primo
    print('\n{} é divisível apenas por 1 e {}, por isso é um número primo.'.format(num,num))
else:
    print('\n{} é divisível por {} números, por isso não é um número primo.'.format(num,soma))

#Diz se a frase inserida é um palíndromo
frase = input('Digite uma frase: ').strip().upper() #letras em maiúsculas
frase = frase.split() #tira os espaços
frase = ''.join(frase) #junta tudo
fraseinvert = frase[::-1] #deixa a string de tras pra frente

cont = 0
print('O inverso de {} é {}.'.format(frase,fraseinvert))

if frase == fraseinvert:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
'''
for aux in range(0,len(frase)):
    if frase[cont] == fraseinvert[cont]:
        cont = cont + 1
if cont == len(frase):
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
'''
#Lê 7 anos de nascimento e diz quantas pessoas já são maiores de idade e quantas não são.
from datetime import date
print('Digite o ano de nascimento de 7 pessoas:')
maiores = 0
menores = 0

for aux in range(0,7):
    ano = int(input('{}° ano: '.format(aux+1)))
    if date.today().year - ano >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1

print('{} pessoas são maiores de idade e {} não são.'.format(maiores,menores))

#Lê o peso de 5 pessoas e diz qual foi o maior e menor pesos lidos
ano = 0
maior = 0
menor = 999999
print('Digite 5 pesos')
for aux in range(0,5):
    peso = float(input('{}° peso: '.format(aux+1)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso digitado foi {}Kg e o menor foi {}Kg.'.format(maior,menor))

#Lê nome, idade e gênero de 4 pessoas e diga: a média das idades do grupo, o nome do homem mais velho e quantas mulheres com menos de 20 anos
soma = 0
velhonome = '0'
velhoidade = 0
fem20 = 0

for aux in range(1,5):
    print('----- {}ª PESSOA -----'.format(aux))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    genero = input('Gênero [M/F]: ')

    soma += idade #soma as idades

    if genero in 'Mm': #se for homem armazena o valor mais alto e o nome
        if idade > velhoidade:
            velhoidade = idade
            velhonome = nome

    if genero in 'Ff' and idade < 20: #conta quantas mulheres tem menos de 20 anos
        fem20 += 1

print('A média das idades do grupo é {}.\n'
      'O homem mais velho se chama {} com {} anos.\n'
      'Há {} mulheres com menos de 20 anos.'.format(soma/aux, velhonome, velhoidade, fem20))