def perguntar():
    return input("\n=============MENU=============\n" +
          "<I> - Para Inserir um usúario\n" +
          "<P> - Para Pesquisar um usúario\n" +
          "<E> - Para Excluir um usúario\n" +
          "<L> - Para Listar todos os usúarios: ").upper()


def inserir(usuarios):
    print("\n===========CADASTRO===========")
    usuarios[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a última data de acesso: "),
                                                   input("Qual a última estação acessada: ").upper()]

def pesquisar(usuarios):
    print("\n===========PESQUISA===========")
    chave = input("Digite o login do usúario: ").upper()
    print(usuarios.get(chave))

def excluir(usuarios):
    print("\n===========EXCLUIR===========")
    chave = input("Digite o login do usúario: ").upper()
    usuarios.pop(chave)
    return "Usúario removido com sucesso"

def listar(usuarios):
    print("\n===========LISTA===========")
    print(usuarios)