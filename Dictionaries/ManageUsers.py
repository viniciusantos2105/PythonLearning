from Functions import *

usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        opcao = inserir(usuarios)
    if opcao == "P":
        opcao = pesquisar(usuarios)
    if opcao == "E":
        opcao = excluir(usuarios)
    if opcao == "L":
        opcao = listar(usuarios)
    opcao = perguntar()