llista = []
while True:
    valor = input("Fica un numero:")
    if valor == "final":
        break
    else:
        llista.append(int(valor))
resultat = 0
llista.sort()
print(llista[0])
