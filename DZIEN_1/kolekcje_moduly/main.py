#import dane
#import dane as dn
from dane import rocznik as rok
from dane import samochod as sam

from samochodowe_funkcje.sfunckje import czytaj_lata,czytaj_sam

from klasazbiorcza.cdklasa import CDDane


print("_________ wywołanie bezpośrednie ________")
print(rok)
print(sam)

print("_________ wywołanie przez funkcje ________")
czytaj_lata(rok)
czytaj_sam(sam)

print("_________ wywołanie przez obiekt ________")
cd = CDDane(rok,sam)
cd.czytaj_l()
cd.czytaj_s()
