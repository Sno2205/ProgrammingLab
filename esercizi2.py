#Funzione che crea una lista di n elementi
def CreaLista(n):
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
    list = CreaLista(numero)
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
    list = CreaLista(numero)
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

scambio()