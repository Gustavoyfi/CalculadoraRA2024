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
    while True:
        linha()
        print("ESCOLHA UMA OPÇÃO".center(60))
        linha()
        op = str(input(" [1] Conjuntos numéricos\n [2] Função do segundo grau\n [3] Funções exponenciais\n [4] Matrizes\n [5] Sair\n >>> "))
        if op == "5":
            print("Você saiu da calculadora.")
            break
        elif op not in "12345":
            print("Opção inválida! Tente novamente.")
            sleep(.5)
            continue
        if op == "1":
            while True:
                A.clear()
                B.clear()
                A = []
                B = []
                A.append(int(input("Informe o conjunto A: ")))
                B.append(int(input("Informe o conjunto B: ")))
                while True:
                    linha()
                    print("ESCOLHA UMA OPERAÇÃO PARA OS CONJUNTOS".center(60))
                    linha()
                    oc = str(input(f" [1] Verificar se A é subconjunto próprio de B \n [2] Realiza operação de União\n [3] Calcular intersecção\n [4] Calcular diferença\n \n [5] Informar outros conjuntos\n [6] Sair para menu inicial\n >>>"))
                    if oc == "5":
                        break
                    elif oc == "6":
                        break 
                    elif oc not in "123456":
                        print("Operação inválida! Tente novamente.")
                        sleep(.5)
                        continue
        elif op == "2":
        elif op == "3":
            while True:
                linha()
                print("ESCOLHA UMA OPERAÇÃO PARA A FUNÇÃO EXPONENCIAL".center(60))
                linha()
                oc = str(input(f" [1] Verificar se é crescente ou decrescente \n [2] Cálcular função em X pedido\n [3] Gerar gráfico\n \n [4] Informar outra função exponencial\n [5] Sair para menu inicial\n >>>"))
        elif op == "4":
            while True:
                linha()
                print("ESCOLHA UMA OPERAÇÃO PARA OS CONJUNTOS".center(60))
                linha()
                oc = str(input(f" [1] Determinante (2x2 ou 3x3) - Verificar se é matriz quadrada \n [2] Multiplicação\n [3] Matriz transposta\n \n [5] Informar outra matriz\n [6] Sair para menu inicial\n >>>"))
menu()
from Reserva import linha
def segundograu(a,b,c):
    a = int(input("Informe o (a) da função:"))
    b = int(input("Informe o (b) da função:"))
    c = int(input("Informe 0 (c) da função:"))
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
        yv = -(d)/4*