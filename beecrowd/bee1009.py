nomeVendedor = input()
salario = float(input())
comissao = float(input())

salarioFinal = salario + ((comissao * 15 ) / 100)
print(f'TOTAL = R$ {salarioFinal:.2f}')