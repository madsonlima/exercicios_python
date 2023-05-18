#Digitar um número de 0 a 20 e escrever por extenso
num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','valor','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
aux = -1
while aux > 20 or aux < 0:
    aux = int(input('Digite um número de 0 a 20: '))
print(f'Você digitou o número {num[aux]}!')

#Ranking de dano causado de uma partida
champs = ('Caitlyn','Mordekaiser','Gwen','Fiora','Miss Fortune')

for aux in range(0,2):
    print(f'O {aux+1}° colocado foi {champs[aux]}.')
print('-'*20)

for aux in range(2,len(champs)):
    print(f'O {aux + 1}° colocado foi {champs[aux]}.')
print('-'*20)

champs = sorted(champs)
print('Em ordem alfabética:')
for aux in range(0,len(champs)):
    print(f'{champs[aux]}')
print('-' * 20)

print(champs)
print('Fiora está na {}ª posição.'.format(champs.index('Fiora')+1))

#Gera 5 números aleatórios e coloca em uma tupla, mostra os números e diz qual é o menor e o maior.
from random import randint
tupla = (randint(0,9)), (randint(0,9)), (randint(0,9)), (randint(0,9)), (randint(0,9))
print(tupla)
#tupla = sorted(tupla)
print('O primeiro valor foi {}.\n'
      'O último valor foi {}.'.format(tupla[0],tupla[len(tupla)-1]))

print('Valor mínnimo: {}\n'
      'Valor máximo: {}'.format(min(tupla),max(tupla)))

#Lê e armazena 4 valores em uma tupla, diz quantas vezes apareceu o valor 9, em que posição foi adicionado o primeiro valor 3 e quais foram os números pares
valores = (int(input("Digite um valor: ")),
           int(input("Digite um valor: ")),
           int(input("Digite um valor: ")),
           int(input("Digite um valor: ")))
print(valores)

nove = 0
if 9 in valores:
    #print(f"O valor 9 apareceu {valores.count(9)} vezes.")
    for aux in range(0,len(valores)): #não precisa definir o tamanho da tupla, mas só fui descobrir depois
        if valores[aux] == 9:
            nove += 1
    print(f"O número 9 apareceu {nove} vezes.")
else:
    print("Não há nenhum número 9.")

aux = 0
if 3 in valores:
    #print(f"O valor 3 apareceu na {valores.index(3)}ª posição.")
    if valores.count(3) == 1:
        for aux in range(0,len(valores)):
            if valores[aux] == 3:
                print(f"O único valor 3 apareceu na posição {aux+1}.")
    elif valores.count(3) > 1:
        for aux in range(0,len(valores)):
            if valores[aux] == 3:
                print(f"O primeiro valor 3 apareceu na posição {aux + 1}.")
                break
else:
    print("Não há nenhum número 3.")

aux = par = 0
for aux in valores: #não precisa definir o tamanho da tupla!!!!!!!!!!!!!!!!!!!!!
    if aux % 2 == 0: #nesse caso o aux vai receber o valor daquela posição específica! Não precisa de valores[aux]!
        print(f"{aux}, ",end='')
        par += 1
if par == 0:
    print("Não foram digitados números pares.")
elif par == 1:
    print("este foi o único número par digitado.")
else:
    print("estes foram todos os números pares digitados.")

#Criar uma tupla com materias e seus preços, no final mostrar uma listagem de preços, organizando os dados em forma tabular.
materiais = ('Lápis', 1.75,
             'Borracha', 2,
             'Caderno', 15.9,
             'Estojo', 25,
             'Transferidor', 4.2,
             'Compasso', 9.99,
             'Mochila', 120.32,
             'Caneta', 0.5,
             'Livro', 34.9
)
print('-'*39)
print(f'{"LISTAGEM DE PREÇOS":^39}') #centraliza de acordo com um tamanho
print('-'*39)
for posicao in range(0,len(materiais)): #aqui precisa definir o tamanho
    if posicao % 2 == 0:
        print(f'{materiais[posicao]:.<30}',end='') #alinha à esquerda e completa até o valor 30 com pontos
    else:
        print(f'R${materiais[posicao]:>7.2f}') #alinha à direita e completa até o valor 7 com espaço em branco e com duas casas do float
print('-'*39)

#Criar uma tupla com várias palavras (não usar acentos) e depois mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender','programar','linguagem','python','curso','gratis',
            'estudar','praticar','trabalhar','mercado','programador','futuro')

item = 0
for itematual in palavras:
    print(f'\nEm {itematual.upper()} temos: ',end='')
    for letraatual in palavras[item]:
        if letraatual.lower() in 'aáàãâeéèêiíìîoóòõôuúùû':
            print(f'{letraatual} ',end='')
    item += 1
