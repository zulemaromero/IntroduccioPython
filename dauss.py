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
