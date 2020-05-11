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

    def stevio_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
    
    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke:
                return False
        return True

     #all([a, b, c])   preveri ali so vsi true
    #to pomen a and b and c
    #return all(c in self.crka for c in self.geslo)

    
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())
    
    def pravilni_del_gesla(self):
        trenutno = ""
        for crka in self.geslo:
            if crke in self.crke:
                trenutno += crka
            else:
                trenutno += "_"
        return trenutno


    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()

        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke.append(ugibana_crka)
        
        if ugibana_crka in self.geslo:
            #kle je uganil, preverjamo ce je zmagu
            if selg.zmaga()
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else: 
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


def nova_igra():
    nakljucna_beseda = random.choice(bazen_besed)
    return Igra(nakljucna_beseda)
        






