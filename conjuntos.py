def linha():
    print("=" * 60)
def menu_conjuntos():
    while True:
        A = []
        B = []
        A.append(int(input("Informe o conjunto A (separando os números com vígula): ")))
        B.append(input("Informe o conjunto B (separando os números com vígula): "))
        for i in A:
            if type(i) == str and type(i) != ",":
                print("Conjunto A inválido! Informe novamente!")
                continue
            elif i == " ":
                print("Conjunto A inválido! Informe novamente!")
                continue
            else:
                break
        for i in B:
            if type(i) == str and type(i) != ",":
                print("Conjunto B inválido! Informe novamente!")
                continue
            elif i == " ":
                print("Conjunto B inválido! Informe novamente!")
                continue
            else:
                break
        oc = str(input(f" [1] Verificar se A é subconjunto próprio de B \n [2] Realiza operação de União\n [3] Calcular intersecção\n [4] Calcular diferença\n \n [5] Informar outros conjuntos\n [6] Sair para menu inicial\n >>>"))
        if oc == "5":
            A.clear()
            B.clear()
            break
        elif oc == "6":
            break
        elif oc not in "123456":
            print("Operação inválida! Tente novamente.")
            sleep(.5)
            continue

menu_conjuntos()