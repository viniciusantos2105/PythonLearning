import math

ponto1 = input().split(" ")
ponto2 = input().split(" ")

x1, y1 = ponto1
x2, y2 = ponto2

distancia = ((float(x2) - float(x1)) * (float(x2) - float(x1))) + ((float(y2) - float(y1)) * (float(y2) - float(y1)))
raiz = math.pow(distancia, 1/2)
print(f'{raiz:.4f}')