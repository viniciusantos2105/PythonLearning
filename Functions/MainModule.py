from FunctionIdentification import *

minhaLista=[]
print("\n=====Preenchendo=====")
preencherInventario(minhaLista)
print("\n=====Exibindo=====")
exibirInventario(minhaLista)

print("\n=====Pesquisando=====")
localizarPorNome(minhaLista)
print("\n=====Alterando=====")
depreciarPorNome(minhaLista, 20)

print("\n=====Excluindo=====")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("\n=====Resumindo=====")
resumirValores(minhaLista)