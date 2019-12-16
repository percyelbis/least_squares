#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### Digitado por usuario
def crear_matriz(f, c):
    
    '''f:filas, c:columnas-->retorna filas
        y digitado por el usuario'''
    m = [] # Lista vacia
    for i in range(f):
        # crea una linea i
        flinea = [] # lista vacia
        for j in range(c):
            valor = float(input("Digite el valor [" +str(i) + "][" + str(j) + "]"))
            flinea.append(valor)
        # add f to flinea
        m.append(flinea)
    return m

def c_mat():
    filas = int(input("Ingrese numero de filas : "))
    col = int(input("Ingrese numero de columnas : "))
	
    return crear_matriz(filas, col)
