#Lê o nome e a média de um aluno, verifica se aprovado e depois mostra o conteúdo da estrutura
aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))

if aluno['Média'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Situacao'] = 'Recuperação'
else:
    aluno['Situacao'] = 'Reprovado'
print('=-' * 30)

for k, v in aluno.items():
    print(f'{k}: {v}')

print(f'O aluno {aluno["Nome"]} obteve média {aluno["Média"]}, portanto está {aluno["Situacao"]}.')

#4 jogadores jogam um dado e armazenar em um dicionario. No final mostrar o dicionário em ordem, com o vencedor com o maior número tirado.
from random import randint
from time import sleep
from operator import itemgetter
jogos = dict()
ranking = dict()

for aux in range(0, 4):
    dado = randint(1, 6)
    print(f'Player {aux} jogou o dado... ',end='')
    sleep(0.5)
    print(f'Deu {dado}!')
    jogos[aux] = dado           #criei um dicionário com os dados por id.
    if aux == 0:
        maior = dado
    else:
        if dado > maior:
            maior = dado

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)            #cria uma lista com os valores de jogos ordenados pelo valor na posição 1 (dado), inversamente
print('='*30)

for aux, pos in enumerate(ranking):                           #como é lista, fazer com enumerate
    print(f'{aux+1}° lugar: Player {pos[0]} com {pos[1]}')
#tbm funcionou
#aux = 1
#for k, v in ranking:
#    print(f'{aux}° lugar: Player {k} com {v}')
#    aux += 1

#Ler nome, ano de nascimento e carteira de trabalho (0 se não tiver), e cadastrar o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
ficha = dict()

ficha['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
ficha['Idade'] = date.today().year - nascimento             #também funciona: datetime.now().year se importar datetime
ficha['Carteira'] = int(input('Carteira de trabalho (0 se não tiver): '))

if ficha['Carteira'] != 0:
    ficha['Contratação'] = int(input('Ano de contratação: '))
    ficha['Salário'] = float(input('Salário: R$'))
    ficha['Aposentadoria'] = ficha['Idade'] + ((ficha['Contratação'] + 35) - date.today().year)         #cálculo de aposentadoria

print('='*30)
for k, v in ficha.items():
    if v == ficha['Carteira']:
        print(f'CTPS: {ficha["Carteira"]}')
    else:
        print(f'{k}: {v}')

#Lê nome do jogador, quantas partidas jogou e quantos gols em cada partida. Mostrar o total.
jogador = dict()
gols = list()
aux = 0

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for aux in range(0, jogador['partidas']):
    gols.append(int(input(f'    Quantos gols fez no {aux+1}° jogo? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols[:])

print('='*30)
print(jogador)

print('='*30)
for k, v in jogador.items():
    print(f'O campo - {k} - tem o valor - {v} -.')

print('='*30)
print(f'{jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for aux in range(0, jogador['partidas']):
    print(f'    Na {aux+1}° partida fez {gols[aux]}.')
print(f'Um total de {jogador["total"]} gols.')

#Leia nome, sexo e idade de várias pessoas. Mostrar quantas pessoas foram cadastradas, a média de idade, uma lista com as mulheres e uma lista de pessoas com idade acima da média.
pessoa = dict()
grupo = list()
#mulheres = list()
#acimamed = list()

continuar = 'S'
media = 0

while continuar in 'S':
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    while pessoa['sexo'] not in 'MF':
        print('Por favor, apenas M (masculino) ou F (feminino).')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    pessoa['idade'] = int(input('Idade: '))

    media += pessoa['idade']        #faz a somatória
    grupo.append(pessoa.copy())     #faz a cópia do dicionário dentro da lista.
    continuar = str(input('Continuar? [S/N] ')).upper()
    while continuar not in 'SN':
        print('Por favor, apenas S (sim) ou N (não).')
        continuar = str(input('Continuar? [S/N] ')).upper()
    print('=' * 30)

media = media / len(grupo)
#for aux in range(0, len(grupo)):         #outro jeito que eu tinha feito
#    if grupo[aux]['sexo'] in 'F':
#        mulheres.append(aux)
#    if grupo[aux]['idade'] > media:
#        acimamed.append(aux)

print('='*30)
print(f'{len(grupo)} pessoas foram cadastradas.\n'
      f'Média das idades: {media}.')
print('='*30)
print('Mulheres cadastradas:')
for aux in grupo:
    if aux['sexo'] in 'F':
        print(f'{aux["nome"]}, {aux["idade"]} anos.')
print('='*30)
print('Pessoas cadastradas com idade acima da média:')
for aux in grupo:
    if aux['idade'] > media:
        print(f'{aux["nome"]}, {aux["idade"]} anos.')

#print('Mulheres cadastradas:')         #outro jeito que eu tinha feito
#for aux in mulheres:
#    print(f'{grupo[aux]["nome"]}, {grupo[aux]["idade"]} anos.')
#print('='*30)
#print('Pessoas cadastradas com idade acima da média:')
#for aux in acimamed:
#    print(f'{grupo[aux]["nome"]}, {grupo[aux]["idade"]} anos.')

#Lê nome de vários jogadores, quantas partidas jogaram e quantos gols em cada partida. Mostrar tabela com cod., nome, gols e total. Escolher jogador específico para mostrar os dados.
time = list()
jogador = dict()
gols = list()
continuar = 'S'

while continuar in 'S':
    jogador['Nome'] = str(input('Nome do jogador: '))
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    for aux in range(0, jogador['Partidas']):
        gols.append(int(input(f'    Quantos gols fez no {aux+1}° jogo? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols[:])

    gols.clear()
    time.append(jogador.copy())
    continuar = str(input('Continuar? [S/N] ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).upper()

print('='*30)
for aux in time:
    for k, v in aux.items():
        print(f'{k}: {v}; ',end='')
    print('\n','='*30)

verificar = -1
while verificar != 999:
    while verificar not in range(0, len(time)):
        verificar = int(input('Verificar dados de que jogador? [ID][999 encerra] '))
    if verificar == 999:
        break
    if verificar in range(0, len(time)):
        verificar = int(input('Verificar dados de que jogador? [ID][999 encerra] '))
    print(f'Gols de {time[verificar]["Nome"]}:')
    for k, v in enumerate(time[verificar]["Gols"]):
        print(f'No jogo {k+1} fez {v} gols.')

    verificar = -1
    print('=' * 30)

print('Programa encerrado.')

'''
print(f'{jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for aux in range(0, jogador['partidas']):
    print(f'    Na {aux+1}° partida fez {gols[aux]}.')
print(f'Um total de {jogador["total"]} gols.')'''