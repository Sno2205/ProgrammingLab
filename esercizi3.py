from esercizi2 import *

#Funzione che prende una lista di parole e restituisce un dizionario con il conteggio delle occorrenze
def listToDict():
    wordDict = {}
    numero = int(input("Dammi il numero di elementi della lista!!\n"))
    list = CreaLista(numero)

    for i in list:
        if(i in wordDict):
            wordDict[i] +=1
        else:
            wordDict[i] = 1
    
    for chiave, valore in wordDict.items():
        print(f"{chiave}: {valore}")
    
    return wordDict


#Funzione che prende i valori dal file dello shampo
def letturaShampoFile():
    #
    # dates = []
    values = []
    my_file = open('shampoo_sales.csv', 'r')
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            #date = elements[0]
            value = float(elements[1])
            values.append(value)
            #dates.append(date)
    return values

#Funzione che prende da file le vendite degli shampi
def sommaVenditeShampo():
    list = letturaShampoFile()
    somma = sommaLista(list)
    print(f"La somma delle vendite è {somma}")
    return somma



sommaVenditeShampo()