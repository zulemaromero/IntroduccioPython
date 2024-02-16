llista = []
while True:
    valor = input("Fica un numero:")
    if valor == "final":
        break
    else:
        llista.append(int(valor))
resultat = 0
for numero in llista:
    resultat = resultat + numero
print("La suma dels elements de la llista es:", resultat)
