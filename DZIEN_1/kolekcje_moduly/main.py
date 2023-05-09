#import dane
#import dane as dn
from dane import rocznik as rok
from dane import samochod as sam

from samochodowe_funkcje.sfunckje import czytaj_lata,czytaj_sam


print("_________ wywołanie bezpośrednie ________")
print(rok)
print(sam)

print("_________ wywołanie przez funkcje ________")
czytaj_lata(rok)
czytaj_sam(sam)
