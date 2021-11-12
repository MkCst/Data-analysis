# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# importing pandas as pd
import pandas as pd
from random import randint
   
# Leyendo datos
lista = [randint for x in range(10)]
lista2 = [randint for x in range(10)]

data1 = pd.Series(lista, 
                  index=['a','b','c','d','e','f','g','x','y','z'])
data2 = pd.Series(lista2, 
                  index=['a','b','c','d','e','f','g','x','y','z'])


# OPERACIONES UNO A UNO