import math
def pb1a(k,c):
    nr_parole_create = k**c
    print("Nr de parole este", nr_parole_create)
    return nr_parole_create
def pb1b(t_pe_ore,nr):
    nr_parole_create= nr
    timp_total= nr_parole_create/t_pe_ore
    print("Timpul total de testare al parolelor: ", timp_total)
    return timp_total

def pb1c(nr_zile,na,nb):
    timp= nr_zile*24
    x=timp*na/nb
    pb= x/na
    print("Probabilitatea de a sparge parola este:", pb)
def pb2(nr_studenti,nr_calculatoare):
    #aranjamente
    mod_asezare= math.factorial(nr_studenti)/math.factorial(nr_studenti-nr_calculatoare)
    print("Nr moduri de asezare este:",mod_asezare)
def pb3(nr_virusi,nr_foldere):
    #combinari
    nr_posibilitati= math.factorial(nr_foldere)/(math.factorial(nr_virusi)*math.factorial(nr_foldere-nr_virusi))
    print("Nr posibilitati", nr_posibilitati)
def pb4a(ln,lv,ct,cv):
    cazuri_posibile= math.comb(ln+lv,ct)
    c1=math.comb(lv,cv)
    c2=math.comb(ln,ct-cv)
    caz_favorabile=c1*c2
    p=caz_favorabile/cazuri_posibile
    print("probabilitatea sa cumperi calculatoare",p)
def pb4b():
    maxim=0


nr_parole=pb1a(62,8)
timp_total=pb1b(1000000*3600,nr_parole)
pb1c(7,nr_parole,timp_total)
pb2(15,10)
pb3(3,10)
pb4a(13,7,6,3)

