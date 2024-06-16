import math
import random

def felszin(meret):
    felszin=(meret/2)*(meret/2)*math.pi
    return felszin

atmero = int(input("Adja meg a medence átmérőjét: "))
szinek = ["kék","zöld","lila","piros"]
print(f'A medence színe: {random.choice(szinek)}')
print(f'A medencére kellő takarás mérete: {felszin(atmero)} nm')