#Konstante za rezultate ugibanj
STEVILO_DOVOLJENIH_NAPAK  = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

#Konstante za zmago in poraz:
ZMAGA = 'W'
PORAZ = 'X'

bazen_besed = []
with open("besede.txt") as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lover()
        if crke is None:
            self.crke = []
        else:
            self.crke = [c.lower() for c in crke] #tle smo tko nardil, ker ne mores uporabit crke.lower() na seznamu. to uporabljamo za niz


    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]    

    

    

