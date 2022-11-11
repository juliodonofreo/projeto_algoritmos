# coding=utf8
from time import sleep
from modulos.alteracoes import criar_lista
from datetime import datetime


def pesquisar():
    try:
        nome = str(input('quer procurar qual nome? '))
        lista = criar_lista()
        for i in lista:
            if i['nome'] == nome:
                for v in i.values():
                    print(f'id: {i["id"]}')
                    print(f'nome: {i["nome"]}')
                    print(f'numero de telefone: {i["telefone"]}')
                    print(f'aniversario: {i["aniversario"]}')
                    input('leia e aperte enter para continuar. ')
                    # o unico objetivo desse return é finalizar a função inteira, já que o break finalizaria apenas o loop
                    return
        print('nome não encontrado.')
        sleep(1)
    except:
        print('você ainda não registrou nenhum contato.')
        sleep(1)


def listar_todos():
    lista = criar_lista()
    for i in lista:  # acessa cada dicionário localizado na lista e depois as suas chaves/valores
        for k, v in i.items():
            print(f'{k}: {v}')
        sleep(1)
        print()
    input('leia e depois aperte enter para continuar.')


def primeiraletra():
    lista = criar_lista()
    quantidade = 0
    # tudo dentro deste while se resume a verificar se o usuario digitou uma letra ou não
    while True:
        letra = str(input('quer pesquisar por qual letra?').lower())
        if len(letra) != 1:
            print('apenas uma letra por favor. ', end='')
        elif not letra.isalpha():
            print('digite uma letra válida. ', end='')
        else:
            break
    sleep(1)
    for i in lista:
        if i['nome'][0] == letra:
            quantidade += 1
            for k, v in i.items():
                print(f'{k}: {v}')
            sleep(1)
    if quantidade == 0:
        print(f'não foram encontrados nomes que comecem com {letra}')
    print()
    input('leia e depois aperte enter para continuar.')


def aniversariantes():
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
             'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    mes_atual = int(datetime.now().month)
    dia_atual = int(datetime.now().day)
    lista = criar_lista()
    contagem = 0
    # puxa o nome do mês na tupla, já que o modulo datetime gera apenas o número do mês
    print(f'os aniversariantes do mes de {meses[mes_atual-1]} são: ')
    sleep(1)

    try:
        for i in lista:
            if int(i['aniversario'][3:]) == mes_atual:
                if int(i['aniversario'][:2]) == dia_atual:
                    print(f'{i["nome"]}, o aniversário dele/a é hoje! Vá parabenizá-lo')
                    sleep(1)
                else:
                    print(f'{i["nome"]}, o aniversário dele/a é no dia {i["aniversario"][:2]}')
                    sleep(1)
                contagem += 1
        if contagem == 0:
            print(f'não foram encontrados aniversariantes do mês de {meses[mes_atual-1]}')
    except:
        print('ainda não foram adicionados dados.')
    input('aperte enter para continuar: ')
