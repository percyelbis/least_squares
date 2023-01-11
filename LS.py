# -*- coding: utf-8 -*-
"""
Compensación por el metodo de minimos cuadrados
en nivelación - Moldelo Matematico Lineal AX = L + V
"""
# Importar librerias
import numpy as np
# Importar modulo creado
import matriz


print("Ingrese la matriz de diseño")
A = matriz.c_mat()
print("Ingrese el vector de observaciones")
L = matriz.c_mat()

# Pesos 
P = [257.667, 372.446, 137.71, 29.716, 116.125, 205.444,
     367.159, 237.947, 209.715, 30.770, 158.654, 381.997] # matriz de pesos {Distancias}

def ls(A, L, P):
    '''
    A: Matriz de diseño
    L: Vector de Observaciones
    P: Lista de Pesos
    '''
    # Matriz de Pesos
    filas, col = len(P), len(P)
    Pd = np.zeros((filas, col) , float)
    np.fill_diagonal(Pd, list(np.reciprocal(list(map(float,P)))))
    
    # inv((A'*P*A))*A'*P*L
    ATP = np.dot(np.transpose(A), Pd)
    ATPA = np.dot(ATP, A)
    iATPA = np.linalg.inv(ATPA)
    
    # Compensación
    
    X = np.dot(iATPA, np.dot(ATP, L))
    
    # Residuos
    V = np.dot(A, X)- L

    #redundancia
    filas, cols = np.array(A).shape
    r = filas - cols
    # desviacion standar peso unitario
    sigma = np.sqrt(np.divide(np.dot(np.dot(np.transpose(V), Pd), V), r))
    # desviaciones standar para los puntos medidos
    s = np.transpose(sigma*np.diag(np.sqrt(iATPA)))
    
    return print("Elevaciones Ajustadas \n", X,
               "\n----------------------------\n",
               "\nV - Residuos \n", V,
               "\n----------------------------\n",
               "\nQxx  - Covarianza\n", iATPA,
               "\n----------------------------\n",
               "\nSo - Desviación estándar de peso unitario \n", sigma,
               "\n----------------------------\n",
               "\nSx - Desviación Standar de los valores ajustados \n", s,
               "\n----------------------------\n",
               "\nW - Pesos \n", Pd,
               "\n----------------------------\n",
               "\nLocal accuracy al 95%: \n", np.mean(np.dot(1.96,s)), "m")
print("----------------------------")
print("---Imprimiendo resultados---")
print("----------------------------")
print(ls(A,L,P))
print("Gracias Totales!!!")





    
