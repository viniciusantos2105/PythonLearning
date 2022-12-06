dias = int(input())

nAno = dias // 365
dias = dias - nAno*365

nMes = dias // 30
dias = dias - nMes*30

nDia = dias // 1
dias = dias - nDia*1

print('{} ano(s) '.format(nAno))
print('{} mes(s) '.format(nMes))
print('{} dia(s)'.format(nDia))