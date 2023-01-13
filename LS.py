# -*- coding: utf-8 -*-
"""
Compensación por el metodo de minimos cuadrados
en nivelación - Modelo Matematico Lineal AX = L + V
donde:
A = Matriz de diseño
X = Vector de Incognitas
L = Vector de mediciones
V = Vector de Residuos o Ruido
"""
# Importar librerias
import numpy as np
# Importar modulo creado
import matriz


print("Ingrese la matriz de diseño")
A = matriz.c_mat()
print("Ingrese el vector de observaciones")
L = matriz.c_mat()
print("Ingrese la presicion del equipo en mm")
nivel = float(input("mm/km :"))
print("Ingrese el vector de distancias en Km")
P = matriz.c_mat()



def ls(A, L, P):
    '''
    A: Matriz de diseño
    L: Vector de Observaciones
    P: Lista de Pesos
    '''
    # Matriz de Pesos
    filas, col = len(P), len(P)
    Pd = np.zeros((filas, col) , float)
    np.fill_diagonal(Pd, np.reciprocal(np.power(0.001*nivel*np.sqrt(np.array(P).astype(float)),2)))
    
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
               "\nQxx  - Cofactores\n", iATPA,
               "\n----------------------------\n",
               "\nCx  - Covarianza\n", (np.power(sigma,2))*iATPA,
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





    
