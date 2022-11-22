# "r" é feito para ler oque tem dentro do arquivo
with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    #tem o .readline() que lê apenas uma linha do arquivo
    print(conteudo)