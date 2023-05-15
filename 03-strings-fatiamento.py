#Ordenar uma lista ==============================
print("Ordenar uma lista")
lista = [3,4,2,1,9,2,5,7,2,3,6]
print(lista)

li = sorted(lista)
print(li)

lista.sort(reverse=True)
print(lista)

#Utiliza as funções ".is..." para verificar as variáveis e retornar um valor booleano. ==============================
#A variedade das funções é bem maior.

print('Checagem de variável')
n = input('Insira algo:')

print('Tipo primitivo: {}'.format(type(n)))

print('É um número? {}'.format(n.isnumeric()))
print('É uma letra? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('É ASCII? {}'.format(n.isascii()))
print('É um digito? {}'.format(n.isdigit()))
print('É decimal? {}'.format(n.isdecimal()))
print('Está todo em maiúsculas? {}'.format(n.isupper()))
print('Está todo em minúsculas? {}'.format(n.islower()))
print('Só tem espaços? {}'.format(n.isspace()))

# Lê o nome de uma pessoa, mostra tudo em maiúsculas e minúsculas, quantas letras sem contar espaços e quantas letras só no primeiro nome
n1 = input('Digite seu nome completo: ')
print('Maiúsculas: {}'.format(n1.upper()))
print('Minúsculas: {}'.format(n1.lower()))
print('O nome completo contém {} letras.'.format(len(n1)-n1.count(' ')))
n1 = n1.split() #dividiu o nome em uma lista de acordo com os espaços pra mostrar só a primeira posição da lista
print('O primeiro nome é {} e contém {} letras.'.format(n1[0], len(n1[0])))

# Lê um número de 0 a 9999 e mostra seus dígitos separados
n1 = input('Digite um número de 0 a 9999: ')
n1 = ' '.join(n1) #bota um espaço entre cada caractere
n1 = n1.split() #divide cada caractere para cada posição de uma lista, separando pelos espaços entre eles
n1.reverse()
if len(n1) >= 1:
    print('Unidade: {}'.format(n1[0]))
    if len(n1) >= 2:
        print('Dezena: {}'.format(n1[1]))
        if len(n1) >= 3:
            print('Centena: {}'.format(n1[2]))
            if len(n1) >= 4:
                print('Milhar: {}'.format(n1[3]))

# Lê o nome de uma cidade e confere se começa com a palavra santo
n1 = input('Digite o nome da cidade: ').strip()
n1 = n1.split()
if 'SANTO' in n1[0].upper(): #compara com as letrar todas maiusculas para evitar engano de case sensitive
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')

# Lê o nome completo de uma pessoa e diz se tem Silva no sobrenome
n1 = input('Digite o nome completo: ').upper()
n1 = n1.split()
if 'SILVA' in n1:
    print('Com sobrenome Silva')
else:
    print('Sem sobrenome Silva')

# Lê uma frase, mostra quantas vezes aparece a letra A, em que posição aparece primeiro e por último
n1 = str(input('Digite uma frase: ')).strip()
n1 = n1.upper()
print('A letra A aparece {} vezes'.format(n1.count('A')))
i = 0
print('Sua primeira aparição foi na posição {}.'.format(n1.find('A')+1))
print('Sua última aparição foi na posição {}.'.format(n1.rfind('A')+1))
'''
while i <= len(n1)-1:   #tem que ser -1 se não da erro, pois o último espaço é sempre o número de caracteres -1
    if n1[i] == 'A':
        print('Sua primeira aparição foi na posição {}.'.format(i+1))
        break
    i += 1

i = len(n1)-1   #tem que ser -1 se não da erro, pois o último espaço é sempre o número de caracteres -1
while i >= 0:
    if n1[i] == 'A':
        print('Sua última aparição foi na posição {}'.format(i+1))
        break
    i -= 1
'''

# Lê o nome completo de uma pessoa e mostra o primeiro e último nome separadamente
n1 = str(input('Digite seu nome completo: ')).strip()
n1 = n1.split()
print('Primeiro nome: {}\nÚltimo nome: {}'.format(n1[0],n1[len(n1)-1]))