import model
import random
trenutna_igra = model.nova_igra()

def izpis_poraza(igra):
    return f"IZGUBIL SI, geslo je bilo: {igra.geslo}"

def izpis_zmage(igra):
    return f"ZMAGAL SI, geslo je bilo: {igra.geslo}," + f"potreboval si {len(igra.napacne_crke())} ugibov."

def izpis_igre(igra):
    text = (
    f"Stanje gesla: {igra.pravilni.ugibi()} \n "
    f"Imas se {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo.napak()} moznosti za napako."
    )     
    return text


def zahtevaj_vnos():
    return input("Vpisi naslednjo crko:")

def pozeni_vmesnik():
    #naredimo novo igro

    trenutna_igra = model.nova_igra()

    while True:
        print(izpis_igre(trenutna_igra))

        crka = zahtevaj_vnos()

        trenutna_igra.ugibaj(crka)

        if trenutna_igra.zmaga():
            print(izpis_zmage(trenutna_igra))
            return
        if trenutna_igra.poraz():
            print(izpis_poraza(trenutna_igra))
            break


    
    
    
    #ponavljamo:
    #vnos:
    #preveri zmago/poraz:
    #nazaj na vnos:

print(izpis_poraza(trenutna_igra))