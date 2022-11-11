# coding=utf8
from time import sleep


# função central do projeto, sendo a função que irá puxar os dados de dentro do arquivo de texto e jogar em diversos
# dicionários dentro de uma lista, além disso ainda cria o arquivo caso o usuário por algum equívoco tenha o deletado
def criar_lista():
    dicionario = {}
    lista = []
    try:
        with open('dados.txt') as dados:
            linhas = dados.readlines()
            for linha in linhas:
                linha = str(linha).replace('\n', '').split('/')
                dicionario['id'] = int(linha[0])
                dicionario['nome'] = linha[1]
                dicionario['telefone'] = f'{linha[2][:5]}-{linha[2][5:]}' if len(linha[2]) == 9 \
                    else f'{linha[2][:4]}-{linha[2][4:]}'  # telefone formatado conforme o tamanho
                dicionario['aniversario'] = f'{linha[3][:2]}/{linha[3][2:]}'  # aniversario formatado
                lista.append(dicionario.copy())
                dicionario.clear()
    except FileNotFoundError:
        with open('dados.txt', 'w') as dados:
            lista = dados
    return lista


# função que insere novos contatos na agenda, criando também um pequeno id pra cada contato
def inserir():
    lista = criar_lista()
    try:
        id = lista[-1]['id'] + 1  # gera um id com base no maior id registado
    except:
        id = 1  # mas caso não existam id's registrados ele começa do 1
    with open('dados.txt', 'a') as dados:
        dados.seek(0)
        while True:
            while True:
                nome = str(input('digite o nome da pessoa: '))
                if nome == '':
                    print('o nome não pode ficar vazio. ', end='')
                elif not nome.isalpha():
                    print('o nome não pode conter numeros e/ou caracteres especiais. ', end='')
                elif len(nome) == 1:
                    print('nome muito curto, digite um que tenha pelo menos duas letras. ',end='')
                else:
                    break
            while True:
                # pensando que talvez o usuario registre o telefone com uma '-' será feita a devida substituição
                telefone = str(input(f'digite o telefone de {nome}: ')).replace('-', '').strip()
                if len(telefone) != 8 and len(telefone) != 9:
                    print('o telefone só pode ter 8 ou 9 digitos. ', end='')
                else:
                    break
            while True:
                # caso o usuario digite o aniversário com uma '/' no meio ela será desconsiderada
                aniversario = str(input('qual o aniversário da pessoa? (dia/mes) ').replace('/', ''))
                if len(aniversario) != 4:
                    print('aniversario completamente inválido, digite novamente. ', end='')
                elif not aniversario.isdigit():
                    print('o aniversario deve ser uma data. ', end='')
                else:
                    break
            dados.write(f'{id}/{nome}/{telefone}/{aniversario}\n')  # o / será usado como um separador,
            # normalmente eu usaria o espaço, mas é possível que um nome composto seja registrado
            id += 1
            condicao = str(input('quer continuar registrando? [s/n]')).lower()[0]
            if condicao in 'n':
                break


def remover():
    lista = criar_lista()
    try:
        for i in lista:
            for k, v in i.items():
                print(f'{k} = {v}')
            sleep(1)
            print()
        while True:
            try:
                deletar = int(input('quer deletar qual id? os ids serão recalculados. [0 cancela a operação] '))
            except ValueError:
                print('o id deve ser um número, mas não se preocupe, apenas digite novamente. ', end='')
            else:
                # valida o id, caso ele não esteja entre os listados e não seja 0 será recusado
                if (deletar < lista[0]['id'] or deletar > lista[-1]['id']) and deletar != 0:
                    print('id inválido, digite somente um dos mostrados. ', end='')
                else:
                    break
        if deletar == 0:
            print('operação cancelada')
        else:
            with open('dados.txt', 'w') as dados:
                for i in lista:
                    if i['id'] != deletar:  # verifica se o id é o que deve ser deletado, se sim a linha será ignorada
                        dados.write(f'{i["id"] if i["id"] < deletar else i["id"]-1}/'  # recálculo do id
                                    f'{i["nome"]}/{i["telefone"].replace("-","")}'
                                    f'/{i["aniversario"].replace("/", "")}\n')
    except:
        print('ainda não foram registrados dados.')
