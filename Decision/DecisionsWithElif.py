nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doencaContagiosa=input("Suspeita de doença contagiosa? ").upper()

if idade >= 65:
    print("O paciente " + nome + " é prioridade")
elif doencaContagiosa=="SIM":
    print("O paciente " + nome + " deve ser isolado")
else:
    print("O paciente " + nome  + " não é prioridade")
