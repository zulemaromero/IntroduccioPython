numero1 = input("Digues un numero: ")
numero2 = input("Digues un altre numero: ")
try:
    resultat = int(numero1) + int(numero2)
    print(resultat)
except:
    print("ERROR")
