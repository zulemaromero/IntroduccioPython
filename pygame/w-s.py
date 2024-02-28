moviment_pantalla = input("""Per anar amunt presiona "w"
Per anar avall presiona "s" : """)
alçada = 21
posicio = 0
while True:
    moviment_pantalla = input(":")
    if moviment_pantalla == "w":
        posicio = posicio - 1
        if posicio < 0:
            posicio = 0
    elif moviment_pantalla == "s":
        posicio = posicio + 1
        if posicio >= alçada:
            posicio = alçada - 1
    text = ""
    for i in range(alçada):
        if i == posicio:
            text += "*"
        else:
            text += "."
        text += "\n"
    print(text)
    print(posicio)
