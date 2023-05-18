from pacote import titulo


def menu():
    titulo.titulo("\033[0;30;44m Menu principal \033[m")
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar pessoa')
    print('3 - sair do programa')


def inopt(txt='Sua opção: '):
    while True:
        try:
            opcao = int(input(txt))
            if opcao == 1:
                titulo.titulo('\033[0;30;42m MOSTRAR CADASTROS \033[m')
                break
            elif opcao == 2:
                titulo.titulo('\033[0;30;42m CADASTRAR NOVO USUÁRIO \033[m')
                break
            elif opcao == 3:
                titulo.titulo('\033[0;30;42m ENCERRAR PROGRAMA \033[m')
                break
            else:
                print('\033[0;31m[ERRO] Digite uma opção válida.\033[m')
        except (ValueError, TypeError):
            print('\033[0;31m[ERRO] Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31m[ERRO] Entrada de dados interrompida pelo usuário.\033[m')
            opcao = 3
            break

    return opcao


def verificarArquivo(src):
    try:
        a = open(src, 'rt')     # read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(src):
    try:
        a = open(src, 'wt+')    # write text | + cria arquivo se necessário
        a.close()
        print('Arquivo criado com sucesso.')
    except:
        print('Erro na criação do arquivo.')


def mostrarArquivo(src):
    try:
        a = open(src, 'rt')
    except:
        print('Erro ao acessar arquivo.')
    else:
        print('Pessoas cadastradas:')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Nome: {dado[0]:<20}, {dado[1]:<2} anos')
        print(a.read())
    finally:
        a.close()


def cadastrarUsuario(src, nome='Desconhecido', idade=0):
    try:
        a = open(src, 'at')
    except:
        print('Erro 1 ao escrever no arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro 2 ao escrever no arquivo.')
        else:
            print('Registro concluído!')
    finally:
        a.close()