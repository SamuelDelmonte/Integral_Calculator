import numpy as np
import matplotlib.pyplot as plt

n = int(input('n = ')) #Número de subdivisões
intervalo_a = int(input('a = ')) #Início do intervalo "a"
intervalo_b = int(input('b = ')) #fim do intervalo "b"

def graph ():
    eixo_x = []
    eixo_y = []
    
    for x in np.arange(intervalo_a, intervalo_b, 0.01):
        eixo_x.append(x)
        eixo_y.append(1/x)
    
    plt.plot(eixo_x, eixo_y)
    plt.grid()
    plt.show()

def sumEsq(n, intervalo_a, intervalo_b):
    delta_x = (intervalo_b - intervalo_a) / n #Variação entre os subintervalos
    xi = intervalo_a #Valor dos subintervalos
    y = 0 #função que começará como 0
    area = 0 #Área sob a função
        
    for x in np.arange (intervalo_a, intervalo_b, delta_x): #Loop que representa o somatório de f(xi) * Δx
        y = 1 / xi #f(xi)
        area += y * delta_x #Somatório
        xi += delta_x
    
    return area
    
def sumDir(n, intervalo_a, intervalo_b):
    delta_x = (intervalo_b - intervalo_a) / n
    xi = intervalo_a + delta_x
    y = 0
    area = 0
    
    for x in np.arange (intervalo_a, intervalo_b, delta_x):
        y = 1 / xi
        area += y * delta_x
        xi += delta_x
    
    return area
    
def sumMedPoint(n, intervalo_a, intervalo_b):
    delta_x = (intervalo_b - intervalo_a) / n
    xi = intervalo_a
    y = 0
    area = 0
    
    for x in np.arange(intervalo_a, intervalo_b, delta_x):
        xmed = (xi + (xi + delta_x)) / 2
        y = 1 / xmed
        area += y * delta_x
        xi += delta_x
    
    return area
    
def sumTrap():
    area = (sumEsq(n, intervalo_a, intervalo_b) + sumDir(n, intervalo_a, intervalo_b)) / 2
    
    return area
    
graph()
print(f'ESQ({n}) = ', sumEsq(n, intervalo_a, intervalo_b))
print(f'DIR({n}) = ', sumDir(n, intervalo_a, intervalo_b))
print(f'MED({n}) = ', sumMedPoint(n, intervalo_a, intervalo_b))
print(f'TRAP({n}) = ', sumTrap())
