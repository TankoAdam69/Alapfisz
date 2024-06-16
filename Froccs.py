from adatok import Adatok

italok: list[Adatok] = []

szoda_ar = 0
bor_ar = 0

f = open('froccs.txt', 'r', encoding='utf-8')

ar_sor = f.readline()
adatok = ar_sor.strip().split(' ')
szoda_ar = int(adatok[1])
bor_ar = int(adatok[0])

sorok = f.readlines()
for i in range(0, len(sorok), 2):
    italok.append(Adatok(sorok[i], sorok[i+1]))

f.close()

def main():
    elso()
    masodik()
    harmadik()
    negyedik()
    otodik()
    hatodik()
    

def elso():
    print(f'2. feladat: Fröccsök fajtájának száma: {len(italok)}')

def masodik():
    legnepszerubb = italok[0]
    for ital in italok:
        if ital.eladas > legnepszerubb.eladas:
            legnepszerubb = ital

    print(f'3. feladat: A legnépszerűbb keverék: {legnepszerubb.nev}')

def harmadik():
    legtomenyebb = italok[0]
    for ital in italok:
        if ital.tomenyseg > legtomenyebb.tomenyseg:
            legtomenyebb = ital
    print(f'4. feladat: A legtöményebb ital: {legtomenyebb.nev}')

def negyedik():
    froccs: list[str] = []
    for ital in italok:
        if "fröccs" in ital.nev:
            froccs.append(ital.nev)
    print(f'5. feladat: ezekben az italokban szerepel a "fröccs" szó: ')
    print(f'\t{froccs}')

def otodik():
    fogyott_bor = 0
    fogyott_szoda = 0
    ar_bevetel = 0
    dong = 0 
    for ital in italok:
        fogyott_bor += ital.eladott_bor
        fogyott_szoda += ital.eladott_szoda
        ar_bevetel += int(ital.eladott_bor * bor_ar / 10) + int(ital.eladott_szoda * szoda_ar / 10)
    dong = ar_bevetel * 68.61
    print(f'A héten {fogyott_bor} dl bor, {fogyott_szoda} dl szóda fogyott. A heti bevétel {ar_bevetel} Ft volt, ami {dong} Vietnámi dong.')

def hatodik():
    megadott_froccs = input('7. feladat: Adja meg egy fröccs nevét: ')
    for ital in italok:
        if ital.nev == megadott_froccs:
            print(f'\tA fröccs bortartalma: {ital.bor_tartalom}%')
            hetedik(ital)
            break
    else:
        print('Nem létezik.')

def hetedik(keresett):
    for ital in italok:
        if ital.bor_tartalom == 100 - keresett.bor_tartalom:
            print(f'8. feladatt: Ellentétes arányú fröccs: {ital.nev}')
            break
    else: print('Nincs ilyen.')

felesek = []
f = open('felesek.txt', 'w', encoding='utf-8')
for ital in italok:
    if ital.bor_tartalom == 50:
        felesek.append(f'{ital.nev};{ital.eladas}\n')
f.writelines(felesek)
f.close()

main()