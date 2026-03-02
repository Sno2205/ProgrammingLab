#Funzione che crea una lista di n elementi e li somma
def CreaLista():
    list = []
    numero = int(input("Dammi il numero di elementi della lista!!\n"))
    for i in range(numero):
        elemento = int(input(f"Dammi il {i+1} numero!!\n"))
        list.append(elemento)
    somma = sommaLista(list)
    print(f"La somma della Lista di {numero} elementi è {somma}")
    return list

        

#Funzione che somma tutti i valori di una lista
def sommaLista(list):
    somma = 0
    for i in list:
        somma +=i
    return somma

#Funzione che dice se una parola è palindroma con input dentro la funzione
def palindromo():
    parola = input("Dammi una parola!!\n")
    lun = len(parola)
    flag = True
    for i in range(int(lun/2)):
        if(parola[i] != parola[lun-i-1]):
            flag = False
    if(flag):
        print(f"{parola} è palindromo")
    else:
        print(f"{parola} non è palindromo")
    
    return flag

palindromo()