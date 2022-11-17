tabuada=int(input("Digite o numero da tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(1, 11, 1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))