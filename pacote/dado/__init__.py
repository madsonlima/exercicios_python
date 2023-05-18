def lerdinheiro(texto):

    while True:
        num = str(input(texto)).replace(",", ".").strip()
        if num.isalpha() or num == '':
            print(f"\033[0;31mERRO: preço inválido.\033[m")
        else:
            return float(num)


def lerint(txt='Número inteiro: '):
    while True:
        try:
            inteiro = int(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31m[ERRO] Digite um número inteiro válido.\033[m')
            continue    # retorna ao while
        except KeyboardInterrupt:
            print('\033[0;31m[ERRO] Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return inteiro


def lerfloat():
    while True:
        try:
            real = float(input(f'Número real: '))
            break
        except (ValueError, TypeError):
            print('\033[0;31m[ERRO] Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31m[ERRO] Entrada de dados interrompida pelo usuário.\033[m')
            real = 0
            break

    return real

