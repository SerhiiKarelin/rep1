import math
from myerror import *

def srednia_kwad(lista):
    """Zmiana"""
    """Zmiana nowa"""
    if not type(lista) == list:
        raise IBeBack()
    suma = 0
    zmiena = 2
    for i in lista:
        suma += i*i

    return math.sqrt(float(suma)/len(lista))
s""
def srednia_aryt(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma
