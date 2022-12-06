dinheiro = float(input())

cem = dinheiro // 100.00
dinheiro = dinheiro - cem * 100.00

cinquenta = dinheiro // 50.00
dinheiro = dinheiro - cinquenta * 50.00

vinte = dinheiro // 20.00
dinheiro = dinheiro - vinte * 20.00

dez = dinheiro // 10.00
dinheiro = dinheiro - dez * 10.00

cinco = dinheiro // 5.00
dinheiro = dinheiro - cinco * 5.00

dois = dinheiro // 2.00
dinheiro = dinheiro - dois * 10.00

umReal = dinheiro // 1.00
dinheiro = dinheiro - umReal * 1.00

cinquentaCentavos = dinheiro // 0.50
dinheiro = dinheiro - cinquentaCentavos * 0.50

vinteCincoCentavos = dinheiro // 0.25
dinheiro = dinheiro - vinteCincoCentavos * 0.25

dezCentavos = dinheiro // 0.10
dinheiro = dinheiro - dezCentavos * 0.10

cincoCentavos = dinheiro // 0.05
dinheiro = dinheiro - cincoCentavos * 0.05

umCentavo = dinheiro // 0.01
dinheiro = dinheiro - umCentavo * 0.01

print("NOTAS:")
print('{} nota(s) de R$ 100,00'.format(int(cem)))
print('{} nota(s) de R$ 50,00'.format(int(cinquenta)))
print('{} nota(s) de R$ 20,00'.format(int(vinte)))
print('{} nota(s) de R$ 10,00'.format(int(dez)))
print('{} nota(s) de R$ 5,00'.format(int(cinco)))
print('{} nota(s) de R$ 2,00'.format(int(dois)))
print("MOEDAS:")
print('{} moeda(s) de R$ 1,00'.format(int(umReal)))
print('{} moeda(s) de R$ 0,50'.format(int(cinquentaCentavos)))
print('{} moeda(s) de R$ 0,25'.format(int(vinteCincoCentavos)))
print('{} moeda(s) de R$ 0,10'.format(int(dezCentavos)))
print('{} moeda(s) de R$ 0,05'.format(int(cincoCentavos)))
print('{} moeda(s) de R$ 0,01'.format(int(umCentavo)))

