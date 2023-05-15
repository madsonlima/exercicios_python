def titulo(tit):
    tamanho = len(tit) + 6
    print('-' * tamanho)
    print(f'   {tit}')
    print('-' * tamanho)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
titulo('Função: Obrigatoriedade de voto')


def votoObrigatorio(ano):
    from datetime import date       # Importação local. Prática que economiza memória.

    idade = date.today().year - ano
    if idade <= 15:
        return f'Idade: {idade}, VOTO NEGADO'
    elif 15 < idade < 18 or idade >= 65:
        return f'Idade: {idade}, VOTO OPCIONAL'
    else:
        return f'Idade: {idade}, VOTO OBRIGATÓRIO'


ano = int(input('Ano de nascimento: '))
print(votoObrigatorio(ano))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
titulo('Função: Fatorial com show=True/False e help()')


def fatorial(num, show=False):
    """
    -> Calcula a equação fatorial de um número, podendo mostrar os números multiplicados ou não.
    :param num: Número de qual se quer calcular o fatorial.
    :param show: [default: False] Switch para os números multiplicados do cálculo serem mostrados ou não.
    :return: O número final do cálculo.
    """
    fator = 1
    if show:
        for pos in range(num, 1, -1):
            fator *= pos
            print(f'{pos} * ', end='')
        return f'1 = {fator}'
    else:
        for pos in range(num, 0, -1):
            fator *= pos
        return f'{num}! = {fator}'


help(fatorial)

num = int(input('Número: '))
mostrar = str(input('Mostar números multiplicados? [s][n] '))
if mostrar in 'sS':
    print(fatorial(num,True))
else:
    print(fatorial(num))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
titulo('Função: Jogador e gols com parâmetros opcionais')


def jogador(nome = '< desconhecido >', gols = 0):
    return f'O jogador {nome} fez {gols} gols no campeonato.'


nome = str(input('Nome: '))
gols = str(input('Gols: '))

if gols.isnumeric():        # Confere se gols é uma str numérica, então a transforma em uma int, ou não.
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':      # Elimina os espaços vazios para verificar se foi escrito algo.
    print(jogador(gols=gols))
else:
    print(jogador(nome, gols))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
titulo('Função: Recriar int(input())')


def lerInt(txt):
    print(f'{txt}',end='')
    inp = str(input())
    while not inp.isnumeric():
        print('\033[0;31m[ERRO] Digite um número inteiro válido.\033[m')
        inp = str(input(txt))
    return inp


n = lerInt('Digite um número: ')
print(f'Você digitou o número {n}')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
titulo('Função: Ler notas e mostrar a situação com dicionário')


def notas(* num, sit=False):
    lista = list()
    for aux in num:
        lista.append(aux)

    lista.sort(reverse=True)
    media = sum(lista) / len(lista)
    if media > 6:
        situacao = 'BOA'
    else:
        situacao = 'RUIM'

    dicionario = {'Total:':sum(lista),
                  'Maior:':lista[0],
                  'Menor:':lista[len(lista)-1],
                  'Média:':media,
                  'Situação:':situacao
                  }

    if sit:
        return dicionario
    else:
        del dicionario['Situação:']
        return dicionario

"""continuar = 1
listanotas = list()
while continuar > 0:
    listanotas.append(float(input('Nota: ')))
    continuar = int(input('Continuar? [1 = Sim] [0 = Não] '))
resp = notas(listanotas)"""
resp = notas(5.5, 2.5, 3.8, sit=True)     # sit=False
print(resp)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
titulo('Função: Lista de funções do sistema, com cores')
from time import sleep


def acessando(comando):
    print(f'\033[0;30;46m')
    tam = len(comando) + 29
    print('-' * tam)
    print(f'   Acessando o comando {comando}...')
    print('-' * tam)
    print(f'\n\033[m')
    sleep(1)


def ajuda(comando):
    print(f'\033[0;30;47m\n')
    help(comando)
    print(f'\n\n\033[m')


print(f'\033[0;30;42m\n   Manual de ajuda do Python\n\n\033[m')
funcao = input(f'   Função ou biblioteca: [FIM = encerra] >>> ')
print()

while funcao not in 'fimFIM':
    acessando(funcao)
    ajuda(funcao)
    funcao = input(f'   Função ou biblioteca: [FIM = encerra] >>> ')
    print()

print(f'\033[0;30;41m\n   PROGRAMA ENCERRADO\n\n\033[m')
