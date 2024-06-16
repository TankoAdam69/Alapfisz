from iranyitok import Iranyitok

iranyitokuwu: list[Iranyitok] = []
f = open('NFL_iranyitok.txt', 'r', encoding='utf-8')
f.readline()
for sor in f:
    iranyitokuwu.append(Iranyitok(sor))
f.close()

print(f'3.feladat: A statisztikában {len(iranyitokuwu)} irányító szerepel')

print(f'5. feladat: Legjobb irányítók:')


for i in iranyitokuwu:
    if i.iranyitomutato >= 100 and i.meter >= 4000:
        print(f'\t{i.nev} (Irányítómutató: {i.iranyitomutato}, passzok: {i.meter}m.)')

eladott = int(input('6.feladat: eladott labdák száma: '))
f = open('legtobbeladott.txt','w',encoding='utf-8')
for i in iranyitokuwu:
    if i.eladott > eladott:
        f.write(f'{i.nev}\n')
f.close()
        
legtobb:Iranyitok = iranyitokuwu[0]
for i in iranyitokuwu[1:]:
    if i.touchdown > legtobb.touchdown:
        legtobb = i
print('7. feladat: A legtöbb TD-t szerző játékos:')
print(f'\tNeve: {legtobb.nev}')
print(f'\tTD-k száma: {legtobb.touchdown}')
print(f'\tEladott labdák száma: {legtobb.eladott}')

stat = dict()
for i in iranyitokuwu:
    if i.egyetem in stat.keys():
        stat[i.egyetem] += 1
    else:
        stat[i.egyetem] = 1
print('8.feladat: legsikeresebb egyetemek')
for k,v in stat.items():
    if v > 1:
        print(f'\t{k} - {v}')





        