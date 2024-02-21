
import random

print(random.randint(1, 6))

def dau_6():
    import random
    print(random.randint(1, 6))

def daus_6():
    tirades = int(input("Quants daus vols llençar?"))
    for i in range(tirades):
        tirada = random.randint(1,6)
        print("Tirada",i+1,":",tirada)


def dau_x():
    cares = int(input("Quantes cares te el dau?"))
    print(random.randint(1,cares))

def daus_x():
    cares = int(input("Quantes cares te el dau?"))
    num_daus = int(input("Quants daus?"))
    for i in range(num_daus):
        print(random.randint(1,cares))

###########################

import Daus

while True:
    print("""Benvinguts, ntroduiu una de les següents opcions:
    1. Llençar un dau de 6 cares
    2. Llençar més d'un dau de 6 cares
    3. Llençar un dau de cares definides per l'usuari
    4. Llençar més d'un dau de cares definides per usuari
    5. Sortir
    """)
    num = int(input("Escull un numero de les opcions:"))
    if num == 5:
        break
    if num == 1:
        Daus.dau_6()
    if num == 2:
        Daus.daus_6()
    if num == 3:
        Daus.dau_x()
    if num == 4:
        Daus.daus_x()
