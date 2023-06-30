M = int(input("Qual a quantidade de linhas da matriz? "))
N = int(input("Qual a quantidade de colunas da matriz? "))
if M > 10 or N > 10:
    print("M e N devem ser menores ou iguais a 10.")
    exit()

matriz = []
for i in range(M):
    linha = []
    for j in range(N):
        linha.append(int(input(f"Elemento [{i},{j}]: ")))
    matriz.append(linha)

print("VALORES NEGATIVOS:")
for i in range(M):
    for j in range(N):
        if matriz[i][j] < 0:
            print(matriz[i][j])
