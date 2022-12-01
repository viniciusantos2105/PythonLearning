linha = input().split(" ")

pi = 3.14159
A, B, C = linha

areaTriangulo = (float(A) * float(C)) / 2
areaCirculo = pi * (float(C) * float(C))
areaTrapezio = (1/2) * float(C) * (float(A) + float(B))
areaQuadrado = float(B) * float(B)
areaRetangulo = float(A) * float(B)

print(f'TRIANGULO: {areaTriangulo:.3f}')
print(f'CIRCULO: {areaCirculo:.3f}')
print(f'TRAPÉZIO: {areaTrapezio:.3f}')
print(f'QUADRADO: {areaQuadrado:.3f}')
print(f'RETANGULO: {areaRetangulo:.3f}')