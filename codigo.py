def gerarMatriz(nr_linhas,nr_colunas):
    matriz = []

    for i in range(nr_linhas):
        linha = []
        for j in range(nr_colunas):
            elemento = int(input(f"Informe M{i}{j}\n"))
            linha.append(elemento)

        matriz.append(linha)
    return matriz

def imprirmatriz(maatriz):
    for linha in matriz:
        print(linha)

linhas = int(input("Informe o número de linhas da matriz: \n"))
colunas = int(input("Informe o número de colunas da matriz: \n"))
matriz = gerarMatriz(linhas, colunas)
imprirmatriz(matriz)

