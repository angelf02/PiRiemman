#!/usr/bin/env python

#Primero se define el integrando:
def funcionpi(x):
    return 4/(1+x*x)


#Luego, de define la funcion que me va a sumar las areas, es alimentada por: la funcion (integrando), limite inferior, limite superior, y la cantidad de divisiones.
#Defino variables iniciales necesarias.
#Uso un for para iterar el calculo para cada rectangulo.
#Voy sumando las areas, ancho por altura (funcion evaluada en el punto medio de las divisiones).
def riemman(funcion,a,b,div):
    suma=0
    ancho=(b-a)/div
    for n in range(1,div+1):
        suma+=funcion(a+((ancho*n)-(ancho/2)))*ancho
    return suma


#Imprimo el resultado que quiero
print('Pi se estima a: '+str(riemman(funcionpi,0,1,10000)))

