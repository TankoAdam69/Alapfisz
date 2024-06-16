import math
print('szia uram, van buszjegyed cigire?')

# kúp felszín térfogat (kör alapú gúla)

sugár = input('A kúp alapjának sugara: ')
# sugár változó típusa: string
r = float(sugár)

m = float(input('A kúp magassága: '))

s = math.sqrt(r * r + m * m) 

A = r * r * math.pi + r * s * math.pi 

print(f'A megadott kúp felszíne: {A:.2f}')

V = (r * r * m * math.pi) / 3 
print(f'A megadott kúp térfogata: {V}')