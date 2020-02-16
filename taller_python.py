# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 03:11:00 2020

@author: Cristian Camilo Quebtrada
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


vec1 = np.random.randint(10,size=10)
vec2 = np.random.randint(10,None, 10)

"suma de los vectores"
vec3=vec1+vec2
"suma de vectores con funcion definida"
def calc(a, b):
    return a + b
vec4=print(calc(vec1,vec2))
vec4

"concatenar los dos arreglos"
arr2d = np.array([[23, 22, 22, 14, 17, 11, 11,  2, 19, 20],[7, 9, 8, 4, 7, 5, 5, 1, 6, 6]])
print(arr2d)
"encontrar la sumatoria de los valores"
def sumalista(listaNumeros):
    laSuma = 0
    for n in listaNumeros:
        laSuma = laSuma + n
    return laSuma

print(sumalista(arr2d))

"encontrar la media de los valores"
def mediafor(valores):
    sum=0
    for n in valores:
        sum=sum+n
    
    return sum/len(arr2d)

"imprimir los numeros mayores que 5"
print(arr2d[arr2d>5])

# Load CSV using Pandas from URL
import pandas as pd
from IPython.display import display, HTML
data = pd.read_csv('guia_fasecolda.csv')

print(data.columns)

