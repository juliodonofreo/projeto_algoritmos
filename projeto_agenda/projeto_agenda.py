# coding=utf8
from modulos.menu import *
from modulos.pesquisas import *
from modulos.alteracoes import *

while True:
    funcao = menu()
    if funcao == 1:
        inserir()
    elif funcao == 2:
        remover()
    elif funcao == 3:
        pesquisar()
    elif funcao == 4:
        listar_todos()
    elif funcao == 5:
        primeiraletra()
    elif funcao == 6:
        aniversariantes()
    else:
        break
print('até logo')
