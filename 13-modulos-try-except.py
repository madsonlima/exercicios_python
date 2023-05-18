from pacote import titulo
from pacote import valor
from pacote import dado
'''
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
titulo.titulo("Verificação de valor com Pacote > Módulo")

num = float(input("Digite um valor: R$"))

print(f"\n{num} com um acréscimo de 10% fica {valor.aumentar(num, 10, False)}.")
print(f"{valor.real(num)} com um desconto de 10% fica {valor.real(valor.diminuir(num, 10, False))}.")
print(f"O dobro de {valor.real(num)} é {valor.dobro(num)}.")
print(f"A metade de {valor.real(num)} é {valor.metade(num)}.\n")

print(f"RESUMO DO VALOR".center(30))
print("-"*30)
valor.resumo(num, 10, 20)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
titulo.titulo("Função para ler apenas números")

num = dado.lerdinheiro("Digite um preço: R$")
print(num, ": Lido")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
titulo.titulo("Funções para ler apenas números inteiros e reais")

num = dado.lerint()
print(f'Número lido: {num}')
num = dado.lerfloat()
print(f'Número lido: {num}')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
titulo.titulo("Acessibilidade de um site")

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Erro ao acessar pudim.com.br')
else:
    print('pudim.com.br acessado com sucesso')
    # print(site.read())
'''
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from pacote import cadastro

arquivo = 'cadastros.txt'

if not cadastro.verificarArquivo(arquivo):
    print('Arquivo não detectado.')
    cadastro.criarArquivo(arquivo)

opt = 0
while opt != 3:
    if opt == 1:
        # Mostrar conteúdo do arquivo
        cadastro.mostrarArquivo(arquivo)
    elif opt == 2:
        # Cadastra novo usuário
        nome = str(input('Nome: '))
        idade = dado.lerint('Idade: ')
        cadastro.cadastrarUsuario(arquivo, nome, idade)

    cadastro.menu()
    opt = cadastro.inopt()

print('Programa encerrado com sucesso.')