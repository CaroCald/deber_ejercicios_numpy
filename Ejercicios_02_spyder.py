
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 18:37:50 2018

@author: Carolina Calderon
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "C://Users//Carolina//Documents//GitHub//deber_ejercicios_numpy//data//notas_alumnos.csv"

notas_alumnos = pd.read_csv(CSV_PATH,encoding='latin-1')

# Generar tabla de frecuencias
tab = pd.crosstab(index=notas_alumnos["nota"],columns="frecuencia")
print(tab)


plt.bar(tab.index,tab["frecuencia"])
plt.xlabel("Notas del examen")
plt.savefig("notas.png")

                                