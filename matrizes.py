def linha():
    print("=" * 60)


def imprir_matriz(matriz):
    for linha in matriz:
        print(linha)


def gerarMatriz(quantlinhas,quantcolunas):
    matriz = []
    for i in range(quantlinhas):
        linha = []
        for j in range(quantcolunas):
            numero = int(input(f"Informe uma valor para linha {i} e coluna {j}\n"))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def verificar_matriz_quadrada(matriz):
    linha = 0
    coluna = 0
    for i in matriz:
        linha += 1
    for j in matriz[0]:
        coluna += 1
    if linha == coluna:
        return True
    else:
        return False

def determinante(matriz):
    linha = 0
    coluna = 0
    matriz.append([], [])
    for i in matriz:
        linha += 1
    for j in matriz[0]:
        coluna += 1
    if linha != 2 or linha != 3:
        return False
    elif coluna != 2 or coluna != 3:
        return False
    if linha == 3 and coluna == 3:
        for i in range(0,3):
            matriz[3].append(matriz[i][0])
        for i in range(0,3):
            matriz[4].append(matriz[i][1])
        for i in matriz:
            for j in matriz[1]:
                matriz[i][j]*
        return True
    elif linha == 2 and coluna == 2:
        matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        return True

        
def tranposta_matriz(matriz):
    transposta = []
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    for i in range(nlinhas):
        for j in range(ncolunas):
            transposta[j][j] = matriz[i][j]
    return transposta  
    

def menu_matriz():
    while True:
        linhas = int(input("Informe o número de linhas da matriz: \n"))
        colunas = int(input("Informe o número de colunas da matriz: \n"))
        matriz = gerarMatriz(linhas, colunas)
        imprir_matriz(matriz)
        linha()
        print("ESCOLHA UMA OPERAÇÃO PARA OS CONJUNTOS".center(60))
        linha()
        oc = str(input(f" [1] Determinante (2x2 ou 3x3): Verificar se é matriz quadrada \n [2] Multiplicação\n [3] Matriz transposta\n \n [4] Informar outra matriz\n [5] Sair para menu inicial\n >>>"))
        if oc not in '12345':
            print("Operação inválida! Tente novamente.")
            continue
        if oc == '1':
            if verificar_matriz_quadrada(matriz) == True:
                print("Esta matriz é quadrada!")
            elif verificar_matriz_quadrada(matriz) == False:
                print("Esta matriz não é quadrada!")
                continue
            if determinante == False:
                print("Matriz inválida! Tente novamente")
                continue
menu_matriz()