#Funzione che crea una lista di n elementi integer
def CreaListaInt(n):
    list = []
    for i in range(n):
        elemento = int(input(f"Dammi il {i+1} numero!!\n"))
        list.append(elemento)
    return list
        
#Funzione che somma tutti i valori di una lista
def sommaLista(list):
    somma = 0
    for i in list:
        somma +=i
    return somma

def somma():
    numero = int(input("Dammi il numero di elementi della lista!!\n"))
    list = CreaListaInt(numero)
    somma = sommaLista(list)
    print(f"La somma della Lista di {numero} elementi è {somma}")

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

#Funzione che scambia 2 elementi della lista
def scambio():
    numero = int(input("Dammi il numero di elementi della lista!!\n"))
    list = CreaListaInt(numero)
    print("La lista è:\t")
    for num in range(numero):
        print(f"list[{num+1}] = {list[num]},\t")
    i = int(input(f"Dammi un indice da 1 a {numero}!!\n"))-1
    j = int(input("Dammi altro indice da 1 a {numero}!!\n"))-1
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp
    print("La lista è:\t")
    for num in range(numero):
        print(f"list[{num}] = {list[num]},\t")

#Funzione che crea una lista di n elementi 
def CreaLista(n):
    list = []
    for i in range(n):
        elemento = input(f"Dammi il {i+1} elemento!!\n")
        list.append(elemento)
    return list


#Funzione che controlla se 2 liste hanno almeno 1 elemento in comune
def controlloListe():
    numero = int(input("Dammi il numero di elementi della lista!!\n"))
    list = CreaLista(numero)
    numero = int(input("Dammi il numero di elementi della 2 lista!!\n"))
    list2 = CreaLista(numero)
    flag = False

    for i in list:
        if(i in list2):
            flag = True

    if(flag):
        print("C'è elemento in comune")
    else:
        print("No elemento comune")
    
    return flag


#Funzione che data una lista di interi (solo numeri da 0 a 9), restituisce il suo ononimo in italiano
def listNumToIta():
    my_dict = {0: 'Zero', 1: 'Uno', 2: 'Due', 3: 'Tre', 4: 'Quattro', 5: 'Cinque', 6: 'Sei', 7: 'Sette', 8: 'Otto', 9: 'Nove'}
    numero = int(input("Dammi il numero di elementi della lista!!\n"))
    list = CreaListaInt(numero)
    list2 = []
    print("La lista è:\t")
    for i in list:
        print(f"{i}\t")
        list2.append(my_dict[i])
    
    print("La lista è:\t")
    for i in list2:
        print(f"{i}\t")
