#Lê um número e mostra os números adjacentes
a1 = int(input('Digite um número: '))
print('{} < {} < {}'.format(a1-1,a1,a1+1))

#Lê um número e mostra o dobro, triplo e a raiz quadrada
a1 = float(input('Digite um número: '))
print('Dobro: {}\nTriplo: {}\nRaiz quadrada: {}'.format(a1*2,a1*3,a1**(1/2)))

#Lê duas notas e mostra a média
a1 = float(input('Digite a primeira nota: '))
a2 = float(input('Digite a segunda nota: '))
print('A média foi {}'.format((a1+a2)/2))

#Lê um número em metros e converte para centímetros e milímetros
a1 = float(input('Quantos metros? '))
print('Conversão:\nCentímetros: {}\nMilímetros: {}'.format(a1*100,a1*1000))

#Converte reais em dólares
a1 = float(input('Quantos reais você quer converter para dólar? R$'))
print('R${} = US${}'.format(a1,a1*0.19))

#recebe a altura e largura da parede e mostra o quanto de tinta necessário para pinta-la, considerando que cada lata de tinta pinta 2m²
a1 = float(input('Qual a largura da parede em metros? '))
a2 = float(input('Qual a altura da parede em metros? '))
print('A área da parede é {}m² e serão necessárias {} latas de tinta para pintar.'.format(a1*a2,(a1*a2)/2))

#recebe um preço e o mostra com 5% de desconto
a1 = float(input('Qual o preço? R$'))
print('R${} com desconto de 5% é R${}'.format(a1,a1-a1*0.05))

#recebe o valor do salário e mostra com 15% de aumento
a1 = float(input('Digite o valor do salário: R$'))
print('Com um aumento de 15%, o novo valor é: R${}'.format(a1+a1*0.15))

#converte graus celcius em farenheit
a1 = float(input('Qual a temperatura em graus Celcius? ))
print('Sua conversão em Farenheit fica {}°F'.format(((9*a1)/5)+32))

#aluguel de carros
a1 = int(input('Por quantos dias o carro foi alugado? '))
a2 = float(input('Quantos quilometros o carro rodou? '))
a1 = a1 * 60
a2 = a2 * 0.15
print('O valor a pagar é R${:2f}'.format(a1+a2))

#Mostra a tabuada de um número
n = float(input('Tabuada\nDigite um número: '))
print('{0} * 1 = {1}\n{0} * 2 = {2}\n{0} * 3 = {3}\n{0} * 4 = {4}\n{0} * 5 = {5}\n{0} * 6 = {6}\n{0} * 7 = {7}\n{0} * 8 = {8}\n{0} * 9 = {9}'.format(n, n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9))
#{0} é pra pegar sempre o primeiro do format e precisa identificar as outras posições para não embaralhar

#Calculadora ==============================
from math import sqrt
def soma (x,y):
    return x+y

print("Calculadora (+, -, *, /, **, //, %, sqrt).\n# ** (elevação), // (divisão inteira), % (resto da divisão), sqrt (raiz quadrada).")
n1 = float(input("N1 = "))
op = input("Operação = ")

if op == "sqrt":
    print("Resultado:\n",sqrt(n1))
    #print("Raiz quadrada está em manutenção!")

elif op == "+" or op == "-" or op == "*" or op == "/" or op == "**" or op == "//" or op == "%":
    n2 = float(input("N2 = "))
    print("Resultado:")

    if op == "+":
        print(soma(n1,n2))
    elif op == "-":
        print(n1-n2)
    elif op == "*":
        print(n1*n2)
    elif op == "/":
        try:
            print(n1/n2)
        except:
            print("Não é possível dividir por zero.")
    elif op == "**":
        print(n1**n2)
    elif op == "//":
        try:
            print(n1//n2)
        except:
            print("Não é possível dividir por zero.")
    elif op == "%":
        try:
            print(n1%n2)
        except:
            print("Não é possível dividir por zero.")
else:
    print("Operação não identificada.")