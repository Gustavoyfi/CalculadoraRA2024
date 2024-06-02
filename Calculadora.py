from time import sleep

#Linhas
def linha():
    print("=" * 60)


#Menu principal
def menu():
    linha()
    print("ESCOLHA UMA OPERAÇÃO".center(60))
    linha()
    while True:
        op = str(input(" [1] Conjuntos numéricos\n [2] Função do segundo grau\n [3] Funções exponenciais\n [4] Matrizes\n [5] Sair\n >>>"))
        if op in "123456":
            break
        elif op not in "123456":
            print("Operação inválida! Tente novamente.")
            continue
    return op


#Manipulação de strings conjuntos
def trans_float(conjunto):
    lista = conjunto.replace(" ", "")
    lista = lista.split(",")
    floats = []
    cont = -1
    for itens in lista:
        for itens_de_itens in itens:
            if itens_de_itens in "aAbBcCdDeEfFgGhHiIjJkKlLMmNnOopPqQrRsStTuUvVWwxXyYZz ":
                return False
        cont += 1
        floats.append(float(itens))
    return floats


#Cálculo subconjunto próprio
def sub_conj_proprio(list_A, list_B):
    sim_nao = ['sim']
    for itens in list_B:
        if itens in list_A:
            sim_nao[0] = "sim"
        else:
            sim_nao[0] = "não"
            break
    if sim_nao[0] == "sim":
        return True
    elif sim_nao[0] == "não":
        return False
        

#Uniao dos conjuntos
def uniao_conjunto(list_A, list_B):
    uniao = []
    for itens in list_A:
        if itens not in uniao:
            uniao.append(itens)
    for itens in list_B:
        if itens not in uniao:
            uniao.append(itens)
    return uniao


#Intersecção de conjuntos
def interseccao_conjunto(list_A, list_B):
    interseccao = []
    for itens in list_A:
        if itens in list_B:
            if itens not in interseccao:
                interseccao.append(itens)
    if len(interseccao) > 0:
        return interseccao
    else:
        return "Não há intersecção entre os conjuntos."


#Diferença de conjuntos
def diferenca_conjunto(list_A, list_B):
    diferenca = []
    for itens in list_A:
        if itens in list_A and itens not in list_B:
            diferenca.append(itens)
    return diferenca


#Menu dos conjuntos
def menu_conjuntos():
    while True:
        linha()
        a = (input("Informe o conjunto A (separando os números com vígula): "))
        b = (input("Informe o conjunto B (separando os números com vígula): "))
        A = trans_float(a)
        B = trans_float(b)
        if trans_float(a) == False:
            print("Conjunto inválido! Tente novamente.")
            linha()
            continue
        elif trans_float(b) == False:
            print("Conjunto inválido! Tente novamente.")
            linha()
            continue
        while True:
            linha()
            print("ESCOLHA UMA OPERAÇÃO PARA OS CONJUNTOS".center(60))
            linha()
            print("Opções:")
            oc = str(input(f" [1] Verificar se A é subconjunto próprio de B \n [2] Realizar operação de União\n [3] Calcular intersecção\n [4] Calcular diferença\n \n [5] Informar outros conjuntos\n [6] Sair para menu inicial\n >>>"))
            linha()
            if oc == "1":
                if sub_conj_proprio(A, B) == True:
                    print("Sim, o conjunto B é subconjunto de A.")
                else:
                    print("Não, o conjunto B não é subconjunto de A.")
            elif oc == "2":
                uniao = uniao_conjunto(A, B)
                print(uniao)
            elif oc == "3":
                interseccao = interseccao_conjunto(A, B)
                print(interseccao)
            elif oc == "4":
                diferenca_a = diferenca_conjunto(A, B)
                diferenca_b = diferenca_conjunto(B, A)
                print(" As diferenças são: ")
                print(f"  A-B: {diferenca_a}")
                print(f"  B-A: {diferenca_b}")
            elif oc == "5":
                A.clear()
                B.clear()
                break
            elif oc == "6":
                break
            elif oc not in "123456":
                print("Operação inválida! Tente novamente.")
                continue
        if oc =="6":
            break


#Menu da função quadrática
import numpy as np
import matplotlib.pyplot as plt


#Cálculo das raízes
def raizes_seggrau(a,b,c):
    d = (b**2)-4*a*c
    if d < 0:
        print("Não possuí raízes reais: ")
    x1 = (-b+d**(1/2))/(2*a)
    x2 = (-b-d**(1/2))/(2*a)
    print(f"X1 = {x1:.2f}")
    print(f"X2 = {x2:.2f}")


#Cálculo de y
def fx_calculado(a,b,c,x):
    y = a*(x**2)+(b*x)+c
    return y


#Cálculo dos vétices
def maxmin_seggrau(a,b,c):
    d = (b**2)-(4*a*c)
    xv = -b/(2*a)
    yv = -d/(4*a)
    print(f"x do vétice tem valor: {xv}\ny do vértice tem o valor: {yv}")
    if a < 0:
        print("A função tem um valor máximo.")
    elif a > 0:
        print("A função tem um valor minimo.")


"""def trans_floatseg(a,b,c):
    alfabeto = "aAbBCcDdEeFfGgHhIiJjKklLMmNnOoPpQqrRSsTtUuVvwWxXYyzZ"
    if a in alfabeto or b in alfabeto or c in alfabeto:
        return False
    a = float(a)"""


#Menu função segundo grau
def menu_segundograu():
    while True:
        print("f(x)= ax² + bx + c")
        a = float(input("Informe o coeficiente (a) da função: "))
        b = float(input("Informe o coeficiente (b) da função: "))
        c = float(input("Informe o coeficiente (c) da função: "))
    
        """if trans_floatseg(a,b,c) == False:
            print("Valores incorretos! Infome novamente!")
            continue"""
        while True:
            linha()
            print("ESCOLHA UMA OPERAÇÃO PARA A FUNÇÃO DO 2º GRAU".center(60))
            linha()
            oc = str(input(f" [1] Calcular raízes \n [2] Cálcular função em X pedido\n [3] Calcular Vértice\n [4] Gerar gráfico\n \n [5] Informar outra função de 2º grau\n [6] Sair para menu inicial\n >>> "))
            if oc not in "123456":
                    print("Operação inválida! Tente novamente.")
                    continue
            elif oc == "1":
                raizes_seggrau(a,b,c)
            elif oc == "2":
                x = int(input("Dígite um número (X): "))
                y = fx_calculado(a,b,c,x)
                print(f"O valor de f em função de x é: {y}")
            elif oc == "3":
                maxmin_seggrau(a,b,c)
            elif oc == "4":
                def f(x):
                    y = a*(x**2)+(b*x)+c
                    return y
                      #Criando o nosso domínio (Eixo X)
                eixoX = np.arange(-1200,1500,1)
                print(eixoX)

                eixoY = []
                for x in eixoX:
                    y = f(x)
                    eixoY.append(y)

                print(eixoY)
                plt.plot(eixoX, eixoY, label = "F(x)= ax² + bx + c", color = 'b')
                #Título do gráfico
                plt.title("Função do primeiro grau: F(x)= ax² + bx + c")
                plt.legend()
                #Títulos dos eixos
                plt.xlabel("eixo x")
                plt.ylabel("eixo y")
                #Colocar grade no gráfico
                plt.grid(True)
                #Adicionar linha dos eixos
                plt.axhline(y=0,color='k')
                plt.axvline(x=0,color='k')

                #Mostrar gráfico
                plt.show()
                
            elif oc == "5":
                break
            
            elif oc == "6":
                break  
        if oc == 6:
            break


#Menu exponêncial


#Menu função exponencial   
def menu_funcaoexponencial():
    while True:
        ae = float(input("Informe o coeficiente (a) da função: "))
        while True:
            linha()
            print("ESCOLHA UMA OPERAÇÃO PARA A FUNÇÃO EXPONENCIAL".center(60))
            linha()
            oc = str(input(f" [1] Verificar se é crescente ou decrescente \n [2] Cálcular função em X pedido\n [3] Gerar gráfico\n \n [4] Informar outra função exponencial\n [5] Sair para menu inicial\n >>> "))
            if oc not in "123456":
                print("Operação inválida! Tente novamente.")
                continue
            elif oc == "1":
                if ae > 1:
                    print("A função é Crescente!")
                elif ae > 0 and ae < 1:
                    print("A função é Decrescente!")
            elif oc == "2":
                x = float(input("Informe o (x) da função: "))
                y = ae**x
                print(y)
            elif oc == "3":
                def f(x):
                    x = float(input("Informe o (x) da função:  "))
                    y = ae**x
                    return y
                #Criando o nosso domínio (Eixo X)
                eixoX = np.arange(-10,11,1)
                print(eixoX)

                eixoY = []
                y = f(x)
                eixoY.append(y)

                print(eixoY)
                plt.plot(eixoX, eixoY, label = "f(x) = 2x+1", color = 'b')
                #Título do gráfico
                plt.title("Função do primeiro grau: 2x+1")
                plt.legend()
                #Títulos dos eixos
                plt.xlabel("eixo x")
                plt.ylabel("eixo y")
                #Colocar grade no gráfico
                plt.grid(True)
                #Adicionar linha dos eixosaw
                plt.axhline(y=0,color='k')
                plt.axvline(x=0,color='k')

                #Mostrar gráfico
                plt.show()
            elif oc == "4":
                break
            elif oc == "5":
                break    
        if oc == "5":
            break                    


#Código principal
while True:
    op = menu()
    if op == "1":
        menu_conjuntos()
    elif op == "2":
        menu_segundograu()
    elif op == "3":
        menu_funcaoexponencial()
    #elif op == "4":
    #    menu_matrizes()
    elif op == "5":
        linha()
        print("Calculadora desligada!".center(60))
        linha()
        break