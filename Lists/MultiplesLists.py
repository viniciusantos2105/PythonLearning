equipamentos = []
valor = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valor.append(float(input("Valor: ")))
    seriais.append(int(input("Numero do Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("\nEquipamento...: ", (indice+1))
    print("Nome......: ", equipamentos[indice])
    print("Valor.....: ", valor[indice])
    print("Serial....: ", seriais[indice])
    print("Departamento..: ", departamentos[indice])