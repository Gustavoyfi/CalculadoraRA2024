def linha():
    print("=" * 60)
def segundograu():
    while True:
        a = int(input("Informe o (a) da função:"))
        b = int(input("Informe o (b) da função:"))
        c = int(input("Informe o (c) da função:"))
        if a == str or b == str or c == str:
            print("Dígito errado! Informe (a), (b), (c) novamente!")
            continue
        linha()
        print("ESCOLHA UMA OPERAÇÃO PARA A FUNÇÃO DO 2º GRAU".center(60))
        linha()
        oc = str(input(f" [1] Calcular raízes \n [2] Cálcular função em X pedido\n [3] Calcular Vértice\n [4] Gerar gráfico\n \n [5] Informar outra função de 2º grau\n [6] Sair para menu inicial\n >>>"))
        if oc == "1":
            d = (b**2-4*a*c)
            x1 = (-b+d(1/2))/(2*a)
            x2 = (-b-d(1/2))/(2*a)
        if oc == "2":
            d = (b**2-4*a*c)
            xv = -(b)/2*a
            yv = -(d)/4*a
segundograu()
        
