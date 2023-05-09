import metody
from pojazd import Pojazd
from metody import *

pz = Pojazd()

odl = 570
litry = 49
cena_l = 6.31
print(f"spalanie [l/100km]: {pz.spalanie(odl,litry):0.2f}")
print(f"koszty przejazdu na trasie {odl} km -> {pz.kosztprzejazdu(odl,litry,cena_l):0.2f} zł")

print(metody.policz(6,7))
print(metody.policz(7,7.7))
# print(metody.policz(5,5,2))

a:int = 6
print(a)
print(type(a))

a = True
print(a)
print(type(a))

nb = [43,65,12,6,24,78]
nb2 = nb
nb3 = list(nb)
nb4 = nb[:]


print(nb)
print(nb2)
print(nb3)
print(nb4)

nb[2:4] = [0,0,0,0,0]
print(nb)
print(nb2)
print(nb3)
print(nb4)
