from samochodowe_funkcje.sfunckje import *

class CDDane:

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(CDDane)
    
    # fukcja konstrukcyjna init tworzy definicję obiektu
    def __init__(self,lista,slownik):
        self.lista = lista
        self.slownik = slownik

    def czytaj_l(self):
        return czytaj_lata(self.lista)

    def czytaj_s(self):
        return czytaj_sam(self.slownik)

