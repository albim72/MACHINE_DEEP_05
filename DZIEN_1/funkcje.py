def witaj(imie):
    return f"Miło Cię widzieć {imie}."

def konkurs(imie,punkty):
    return f"uczestnik konkursu {imie}, liczba punktów: {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))

print(osoba(konkurs,"Olga",78))

#funkcja wrapper

def startstop(funkcja):
    def wrapper(*args):
        print("Startowanie procesu...")
        funkcja(*args)
        print("Kończenie procesu")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka")

zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} w urodziny")

dmuchanie("świeczek")
