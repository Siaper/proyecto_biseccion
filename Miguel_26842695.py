#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math


def biseccion(f, a, b, ER, N):
    """
    Implementa el Algoritmo de Biseccion y retorna la aproximación de la raiz.

    Parámetros:
    f: función de variable real f(x).
    a: límite inferior del intervalo.
    b: límite superior del intervalo.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """

    i=1
    pm_actual=0
    pm_previo=0
    err=0.1


    while i < N and err > ER:
        pm_previo=pm_actual
        pm_actual=(a+b)/2

        if f(pm_actual)*f(b)<0:
            a=pm_actual
        else:
            b=pm_actual
        
        if i > 1:
            err=math.fabs((pm_actual-pm_previo)/pm_actual)

        print("Iteración:", i, "Punto Medio:", pm_actual, "Error:", err)
        
        i+=1

    return pm_actual


if __name__ == "__main__":
    # Pruebe aquí su función.
    
    f= lambda x: math.exp(-x)-math.log(x)

    print ("Este es el resultado de el punto medio ",biseccion(f,1,1.5,0.01,7))
