import math
import random


d = int(input('Kérem a kör átmérőjét:'))

allatok = ['elefánt', 'macska', 'kutya', 'zsiráf', 'oroszlán']
randomallat = random.choice(allatok)

def korszamitas(d):
    r = d / 2
    print(r)
    terulet = math.pi * r * r
    return terulet

print(f'{korszamitas(d):.2f}  cm^2 és az állat rajta {randomallat}')