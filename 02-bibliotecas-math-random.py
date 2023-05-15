import math
from random import choice, shuffle

# ----- math ----- #

# lê um número com casas decimais e mostra a porção inteira
n1 = float(input('Digite um número com casas decimais: '))
print('A porção inteira de {} é {}'.format(n1, math.trunc(n1)))

# calcula a hipotenusa de um triângulo (raiz quadrada do quadrado dos catetos)
n1 = float(input('Cateto oposto: '))
n2 = float(input('Cateto adjacente: '))
# print('O calculo da hipotenusa deu: {}'.format(math.sqrt(math.pow(n1,2)+math.pow(n2,2))))
print('O calculo da hipotenusa deu: {}'.format(math.hypot(n1, n2)))

# lê um ângulo e mostra o valor do seno, cosseno e tangente
n1 = float(input('Digite o ângulo: '))
print('Seno: {}\nCoseno: {}\nTangente: {}'.format(math.sin(math.radians(n1)), math.cos(math.radians(n1)), math.tan(n1)))

# ----- random ----- #

# recebe o nome de 4 alunos e sorteia pelo nome
# n1 = ['Madson','Afrânio','Carol','João']
i = 0; n1 = []
while i < 4:
    n1.append(input('Digite o nome do aluno {}: '.format(i + 1)))
    i += 1
print('{} vai apagar a lousa!'.format(choice(n1)))

# recebe o nome de 4 alunos e sorteia a ordem de apresentação
i = 0; n2 = []
while i < 4:
    n2.append(input('Digite o nome do aluno {}: '.format(i + 1)))
    i += 1
shuffle(n2)
print('Ordem de apresentação: {}'.format(n2))

'''

# ----- pygame ----- #
#para abrir e reproduzir um arquivo mp3

import pygame # precisa instalar
pygame.init()

pygame.mixer.music.load(musica.mp3)
pygame.mixer.music.play()
pygame.event.wait()

'''