class Iranyitok:
    def __init__(self,sor: str):
        adatok = sor.strip().split(';')
        #Nev;Yardok;Kiserletek;Sikeres;TD passzok;Eladott;Iranyitomutato;Egyetem
        self.nev = adatok[0]
        self.yardok = int(adatok[1])
        self.kiserletek = int(adatok[2])
        self.sikeres = int(adatok[3])
        self.touchdown = int(adatok[4])
        self.eladott = int(adatok[5])
        self.iranyitomutato = float(adatok[6].replace(',','.'))
        self.egyetem = adatok[7]
        self.meter = self.penzvalto(self.yardok)

    def penzvalto(self,yard: int) -> int:
        meter = yard * 0.9144
        return int(meter)
        

