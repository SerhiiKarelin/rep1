import math

def srednia_kwad(lista):
    """Zmiana"""
    """Zmiana nowa"""
    sprawdz(lista)
    if sprawdz(lista) == False:
        raise IBeBack()
    suma = 0
    zmiena = 2
    for i in lista:
        suma += i*i

    return math.sqrt(float(suma)/len(lista))

def sprawdz(lista):
    """
       Opis1
    """
    if type(lista) == list or type(lista) == tuple:
        for i in lista:
            if type(i) == int:
                continue
            else:
                return False
        return True
    return False

print srednia_kwad([1,2,3])