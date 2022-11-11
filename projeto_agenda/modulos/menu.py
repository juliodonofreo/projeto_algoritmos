# coding=utf8
def menu(teste=False):
    if not teste:
        print('-'*40)
        print('bem vindo ao gerenciador de contatos')
        print('-' * 40)
        print('''[0] encerrar
[1] inserir contato
[2] remover contato
[3] pesquisar contato
[4] listar todos
[5] pesquisar por letra
[6] aniversariantes do mes''')
        while True:
            try:
                retorno = int(input('digite aqui: '))
            except ValueError:
                print('por favor digite um número. ',end='')
            else:
                if str(retorno) not in '0123456':
                    print('por favor digite uma função válida. ', end='')
                else:
                    return retorno
    else:
        print('-' * 30)
        print('protótipo do menu'.center(30))
        print('-' * 30)
        print('''[0] encerrar
[1] inserir contato
[2] remover contato
[3] pesquisar contato
[4] listar todos
[5] pesquisar por letra
[6] aniversariantes do mes''')
        while True:
            try:
                retorno = int(input('digite aqui: '))
            except ValueError:
                print('por favor digite um número. ', end='')
            else:
                if str(retorno) not in '0123456':
                    print('função inválida. ')
                else:
                    print('função válida.')
                    if retorno == 0:
                        break


# caso você queira apenas testar o menu, apenas execute o módulo diretamente. nesse caso será ativado um parâmetro
# de teste
if __name__ == '__main__':
    menu(teste=True)
