inventario=[]
resposta = "S"
while resposta == "S":
    equipamento=(input("Equipamento: ").lower(),
    float(input("Valor: ")),
    int(input("Numero Serial: ")),
    input("Departamento: "))
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in  inventario:
    print("\n", "Nome.....: ", elemento[0])
    print("Valor....: ", elemento[1])
    print("Serial...: ", elemento[2])
    print("Departamento.: ", elemento[3])

busca=input("\nDigite o nome do equipamento que deseja buscar: ").lower()
for elemento in inventario:
    if busca==elemento[0]:
        print("Valor...: ", elemento[1])
        print("Serial..: ", elemento[2])

depreciacao=input("Digite o nome do equipamento que será depreciado: ").lower()
print("Valor antigo: ", elemento[1])
elementoDepreciado = [(elemento[1] * 0.9) for elemento in inventario]
print("Novo valor: ", elementoDepreciado[0])

serial=int(input("\nDigite o serial do equipamento que será excluido: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print("Nome.....: ", elemento[0])
    print("Valor....: ", elemento[1])
    print("Serial...: ", elemento[2])
    print("Departamento.: ", elemento[3])

valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))