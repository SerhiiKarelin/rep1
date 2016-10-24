import math
from myerror import *

def srednia_kwad(lista):
    if not type(lista) == list:
        raise IBeBack()
    suma = 0
    for i in lista:
        suma += i*i
    return math.sqrt(float(suma)/len(lista))