# -*- coding: utf-8 -*-
"""
Compensación por el metodo de minimos cuadrados
en nivelación

"""
# Importar librerias
import numpy as np
# Importar modulo creado
import matriz



A = matriz.c_mat() # matriz de los coeficientes de las incognitas
L = matriz.c_mat() # matriz de observaciones

P = [1, 1, 4, 2, 2] # matriz de pesos - matriz diagonal

def ls(A, L, P):
    '''
    Ingresar A: Matriz
    L: Matriz
    P: Lista
    '''
    # Matriz de Pesos
    filas, col = len(P), len(P)
    Pd = np.zeros((filas, col) , float)
    np.fill_diagonal(Pd, P)
    
    # inv((A'*P*A))*A'*P*L
    ATP = np.dot(np.transpose(A), Pd)
    ATPA = np.dot(ATP, A)
    iATPA = np.linalg.inv(ATPA)
    
    # Compensación
    
    X = np.dot(iATPA, np.dot(ATP, L))
    
    # Residuos
    V = np.dot(A, X)- L
    
    return print("Elevaciones Ajustadas \n", X, "\nResiduos \n", V)





# Test Libro Topografia Wolf and Brinker --- 9 Edicicion Pagina 779
'''
A = [[1, 0],
     [1, 0],
     [-1, 1],
     [0, 1],
     [0, 1]]

L = [[796.20],
     [796.24],
     [3.58],
     [799.79],
     [799.73]]
P = [[1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 4, 0, 0],
     [0, 0, 0, 2, 0],
     [0, 0, 0, 0, 2]]
'''






    