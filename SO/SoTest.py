import platform
import getpass

print("Nome maquina.....", platform.node())
print("Arquitetura......", platform.architecture())
print("Sistema Operacional..", platform.system())
print("Versao do SO.....", platform.release())
print("Processador......", platform.processor())
print("Versao do Python..", platform.version())

#getPass consegue pegar o usuario da maquina

print(getpass.getuser())