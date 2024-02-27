input("""Per anar a l'esquerra presiona "a"
Per anar a la dreta presiona "d" 
:""")
posicio = 0
amplada = 20
while True:

    moviment_pantalla = input(":")

    if moviment_pantalla == "a":
        posicio = posicio - 1
    if moviment_pantalla == "d":
        posicio = posicio + 1
    text = ""
    for i in range(amplada):
        if i == posicio:
            text+="*"
        else:
            text += " "
    print(text)
    print(posicio)
