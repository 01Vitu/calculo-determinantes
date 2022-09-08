import numpy as np

print('Digite a ordem da matriz desejada: ')
linhaA, colunasA = int(input()), int(input())


matrizA = []
for i in range(linhaA):
    matrizA.append([0] * colunasA)


print('Digite a matriz A: ')
for linha in range(linhaA):
    for coluna in range(colunasA):
        matrizA[linha][coluna] = float(
            input(f'Digite a posicao do numero: {linha}, {coluna}:  '))

determinante = np.linalg.det(matrizA)
print(determinante)