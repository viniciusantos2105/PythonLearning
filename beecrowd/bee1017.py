kmL = 12
horasGastas = int(input())
velocidadeMedia = int(input())

listrosGastos = horasGastas * (velocidadeMedia / kmL)

print(f'{listrosGastos:.3f}')