
while True:
    print("""Benvinguts a pycalc, introduiu una de les següents opcions:
    0. Sortir
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir""")
    num = int(input("Escull un numero de les opcions:"))
    if num == 0:
        break

    if num == 1:
        suma1 = float(input("Digues un numero per sumar: "))
        suma2 = float(input("Digues un altre numero per sumar: "))
        resultat1 = suma1 + suma2
        print(resultat1)

    if num == 2:
        resta1 = float(input("Digues un numero per restar: "))
        resta2 = float(input("Digues un altre numero per restar: "))
        resultat2 = resta1 - resta2
        print(resultat2)

    if num == 3:
        multiplicar1 = float(input("Digues un numero per multiplicar: "))
        multiplicar2 = float(input("Digues un altre numero per multiplicar: "))
        resultat3 = multiplicar1 * multiplicar2
        print(resultat3)
    if num == 4:
        divisio1 = float(input("Digues un numero per dividir: "))
        divisio2 = float(input("Digues un altre numero per dividir: "))
        resultat4 = divisio1 / divisio2
        print(resultat4)
