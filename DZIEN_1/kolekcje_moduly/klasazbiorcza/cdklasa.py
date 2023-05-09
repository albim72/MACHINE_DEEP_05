from samochodowe_funkcje.sfunckje import *

class CDDane:
    #fukcja konstrukcyjna new tworzy definicję klasy
    def __new__(cls, *args, **kwargs):
        pass

    # fukcja konstrukcyjna init tworzy definicję obiektu
    def __init__(self,lista,slownik):
        self.lista = lista
        self.slownik = slownik

    def czytaj_l(self):
        return czytaj_lata(self.lista)

    def czytaj_s(self):
        return czytaj_sam(self.slownik)
