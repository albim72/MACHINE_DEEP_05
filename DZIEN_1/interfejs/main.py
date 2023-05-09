from pojazd import Pojazd

pz = Pojazd()

odl = 570
litry = 49
cena_l = 6.31
print(f"spalanie [l/100km]: {pz.spalanie(odl,litry):0.2f}")
print(f"koszty przejazdu na trasie {odl} km -> {pz.kosztprzejazdu(odl,litry,cena_l):0.2f} zł")
