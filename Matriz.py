from fractions import Fraction


def remover(A, tirar_i, tirar_j):
    matriz_nova = [[int(0) for _ in range(len(A) - 1)] for _ in range(len(A) - 1)]
    ni = 0
    for i in range(len(A)):
        if tirar_i == len(A) - 1 and ni == 2:
            continue
        nj = 0
        for j in range(len(A)):
            if j != tirar_j:
                matriz_nova[ni][nj] = A[i][j]
                nj += 1
        if i != tirar_i:
            ni += 1
    return matriz_nova


def determinante(A):
    if len(A) != len(A[0]):
        print("A matriz não é quadrada!")
        return A
    resposta = 0
    if len(A) == 2:
        resposta = (A[0][0] * A[1][1]) - (A[1][0] * A[0][1])
        return resposta
    if len(A) > 2:
        for j in range(len(A)):
            resposta += A[0][j] * (-1) ** (j + 0) * determinante(remover(A, 0, j))
        return resposta


def inversa(A):
    matriz_inversa = [[int(0) for _ in range(len(A))] for _ in range(len(A))]
    if determinante(A) == 0:
        print("A inversa dessa matriz não existe!")
        return A
    for i in range(len(A)):
        for j in range(len(A)):
            if len(A) == 2:
                resultado = ((-1) ** (i + j)) * A[i][j]
                matriz_inversa[i][j] = Fraction(resultado, determinante(A))
            if len(A) > 2:
                resultado = ((-1) ** (i + j)) * determinante(remover(A, i, j))
                matriz_inversa[i][j] = Fraction(resultado, determinante(A))
    return matriz_inversa


matriz_5 = [[1, 2, 9, 4, 7], [7, 3, 1, 1, 3], [2, 5, 8, 1, 4], [4, 4, 2, 4, 5], [12, 3, 6, 7, 9]]
matriz_4 = [[1, 2, 9, 4], [7, 3, 1, 1], [2, 5, 8, 1], [4, 4, 2, 4]]
matriz_3 = [[1, 2, 9], [7, 3, 1], [2, 5, 8]]
matriz_2 = [[3, 5], [-7, 2]]

# Coloque a Matriz que vc quiser em B
B = inversa(matriz_3)

print(f"Determinante: {determinante(B)}")
print("Inversa:")
for x in range(len(B)):
    for y in range(len(B)):
        print(B[x][y], end='  ')
    print()

print("\nteste:")
for x in range(len(matriz_3)):
    for y in range(len(matriz_3)):
        print(matriz_3[x][y], end=' ')
    print()
