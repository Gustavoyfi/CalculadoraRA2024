from time import sleep
def linha():
    print("=" * 60)
def funcao_quad(a,b,c):
    d = (b**2-4*a*c)
    x1 = (-b+d(1/2))/(2*a)
    x2 = (-b-d(1/2))/(2*a)
def max_min(a,b,c):
    d = (b**2-4*a*c)
    xv = -(b)/2*a
    yv = -(d)/4*a
def conjunto(a,b):
    lista_a = []
    lista_a.append(a)


def menu():
    linha()
    print("ESCOLHA UMA OPERAÇÃO".center(60))
    linha()
    op = str(input(" [1] Conjuntos numéricos\n [2] Função do segundo grau\n [3] Funções exponenciais\n [4] Matrizes\n [5] Sair\n >>>"))
    return op

def menu_conjuntos():
    while True:
        A = []
        B = []
        linha()
        print("ESCOLHA UMA OPERAÇÃO PARA OS CONJUNTOS".center(60))
        linha()
        A.clear()
        B.clear()
        while True:
            A.append(input("Informe o conjunto A (separando os números com vígula): "))
            B.append(input("Informe o conjunto B (separando os números com vígula): "))
            for i in A:
                if type(i) == str:
                    print("Conjunto A inválido! Informe novamente!")
                    continue
                elif i == " ":
                    print("Conjunto A inválido! Informe novamente!")
                    continue
                else:
                    break
            for i in B:
                if type(i) == str:
                    print("Conjunto B inválido! Informe novamente!")
                    continue
                elif i == " ":
                    print("Conjunto B inválido! Informe novamente!")
                    continue
                else:
                    break
        oc = str(input(f" [1] Verificar se A é subconjunto próprio de B \n [2] Realiza operação de União\n [3] Calcular intersecção\n [4] Calcular diferença\n \n [5] Informar outros conjuntos\n [6] Sair para menu inicial\n >>>"))
        if oc == "5":
            break
        elif oc == "6":
            break 
        elif oc not in "123456":
            print("Operação inválida! Tente novamente.")
            sleep(.5)
            continue

def menu_funcaoquadradica():
    while True:
                linha()
                print("ESCOLHA UMA OPERAÇÃO PARA A FUNÇÃO DO 2º GRAU".center(60))
                linha()
                oc = str(input(f" [1] Calcular raízes \n [2] Cálcular função em X pedido\n [3] Calcular Vértice\n [4] Gerar gráfico\n \n [5] Informar outra função de 2º grau\n [6] Sair para menu inicial\n >>>"))

while True:   
    op = menu()
    if op == "1":
        menu_conjuntos()    
    if op not in "12345":
        print("Operação inválida! Tente novamente.")
        sleep(.5)
        continue
    elif op == "5":
        print("Você saiu da calculadora.")
        break
