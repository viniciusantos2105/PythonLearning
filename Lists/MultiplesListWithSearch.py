equipamentos = []
valor = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: ").lower())
    valor.append(float(input("Valor: ")))
    seriais.append(int(input("Numero do Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

busca=input("\nDigite o nome do equipamento: ").lower()
for indice in range(0, len(equipamentos)):
    if busca==equipamentos[indice]:
        print("\nEquipamento...: " + busca)
        print("Valor...: ", valor[indice])
        print("Serial..: ", seriais[indice])