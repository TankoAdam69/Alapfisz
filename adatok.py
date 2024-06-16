class Adatok:
    def __init__(self, sor1: str, sor2:str):
        adatok = sor2.strip().split(' ')

        self.nev = sor1.strip()
        self.bor = int(adatok[0])
        self.szoda = int(adatok[1])
        self.eladas = int(adatok[2])
        self.tomenyseg = self.bor / self.szoda
        self.eladott_bor = self.eladas * self.bor
        self.eladott_szoda = self.eladas * self.szoda
        self.bor_tartalom = round(self.bor / (self.bor + self.szoda) * 100,2)
        
