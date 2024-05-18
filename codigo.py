import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = 2*x**3 + 1
    return y

#Criando o nosso domínio (Eixo X)
eixoX = np.arange(-10,11,1)
print(eixoX)

eixoY = []
for x in eixoX:
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
#Adicionar linha dos eixos
plt.axhline(y=0,color='k')
plt.axvline(x=0,color='k')

#Mostrar gráfico
plt.show()