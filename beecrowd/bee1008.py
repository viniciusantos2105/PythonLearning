FUNCIONARIO = {int(input()): [int(input()), float(input())]}

NUMBER = int(input())
SALARY = FUNCIONARIO.get(NUMBER)[1] * FUNCIONARIO.get(NUMBER)[0]
print("NUMBER  =", NUMBER)
print(f'SALARY = U$ {SALARY:.2f}')