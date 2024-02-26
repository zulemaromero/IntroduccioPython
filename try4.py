while True:
    llista = [1,3,5,7,9]
    try:
        num= int(input("Digues un numero de la llista:"))
        print(llista[num])
    except:
        print("ERROR")
