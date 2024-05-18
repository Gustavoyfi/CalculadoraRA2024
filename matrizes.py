def linha():
    print("=" * 60)
def matriz():
    while True:
        linha()
        print("ESCOLHA UMA OPERAÇÃO PARA OS CONJUNTOS".center(60))
        linha()
        oc = str(input(f" [1] Determinante (2x2 ou 3x3) - Verificar se é matriz quadrada \n [2] Multiplicação\n [3] Matriz transposta\n \n [5] Informar outra matriz\n [6] Sair para menu inicial\n >>>"))
matriz()