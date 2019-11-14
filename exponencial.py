import numpy as np
import matplotlib.pyplot as plt

n = int(input('n = ')) #Número de subdivisões
intervalo_a = int(input('a = ')) #Início do intervalo "a"
intervalo_b = int(input('b = ')) #fim do intervalo "b"
e = 2.71828 #número de Euler para a função exponencial

def graph (): #Função que plota o gráfico da função dada no devido intervalo
    eixo_x = []
    eixo_y = []

    for x in np.arange(intervalo_a, intervalo_b, 0.01):
        eixo_x.append(x)
        eixo_y.append(e ** (x-1))
    
    plt.plot(eixo_x, eixo_y)
    plt.grid()
    plt.show()

def sumEsq(n, intervalo_a, intervalo_b): #Soma à esquerda
    delta_x = (intervalo_b - intervalo_a) / n #Variação entre os subintervalos
    xi = intervalo_a #Valor dos subintervalos
    area = 0 #Área sob a função
        
    for x in np.arange (intervalo_a, intervalo_b, delta_x): #Loop que representa o somatório de f(xi) * Δx
        y = e ** (xi - 1) #f(xi)
        area += y * delta_x #Somatório
        xi += delta_x
    
    return area
    
def sumDir(n, intervalo_a, intervalo_b): #Soma à direita
    delta_x = (intervalo_b - intervalo_a) / n
    xi = intervalo_a + delta_x
    area = 0
    
    for x in np.arange (intervalo_a, intervalo_b, delta_x):
        y = e ** (xi - 1)
        area += y * delta_x
        xi += delta_x
    
    return area
    
def sumMedPoint(n, intervalo_a, intervalo_b): #Regra do ponto médio
    delta_x = (intervalo_b - intervalo_a) / n
    xi = intervalo_a
    area = 0
    
    for x in np.arange(intervalo_a, intervalo_b, delta_x):
        xmed = (xi + (xi + delta_x)) / 2
        y = e ** (xmed - 1)
        area += y * delta_x
        xi += delta_x
    
    return area
    
def sumTrap(): #Regra do Trapézio
    area = (sumEsq(n, intervalo_a, intervalo_b) + sumDir(n, intervalo_a, intervalo_b)) / 2
    
    return area

def sumSimpson():
    area = (2 * (sumEsq(n, intervalo_a, intervalo_b)) + sumDir(n, intervalo_a, intervalo_b)) / 3
    
    return area
    
graph()
print(f'ESQ({n}) = ', sumEsq(n, intervalo_a, intervalo_b))
print(f'DIR({n}) = ', sumDir(n, intervalo_a, intervalo_b))
print(f'MED({n}) = ', sumMedPoint(n, intervalo_a, intervalo_b))
print(f'TRAP({n}) = ', sumTrap())
print(f'SIMP({n}) = ', sumSimpson())