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

#Funzione creazione file con contenuto scritto in input da utente
def scritturaFile():
    #frase = input("Dammi una frase da scrivere su file!!\n")
    frase = "\nIl gatto e la volpe sono animali.\nIl gatto vive in casa, mentre la volpe vive nel bosco.\nLa volpe e' furba, ma il gatto e' agile.\nOggi ho visto un gatto nel giardino."
    my_file = open('test.txt', 'a')
    my_file.write(frase)
    my_file.close()


#Funzione che preso un file conta il numero di volte in cui una parola è scritta (deve essere esattamente quella)
def ricorrenzaParolaFile():
    parola = input("Dammi un parola!!")
    cont = 0
    my_file = open('test.txt', 'r')
    for line in my_file:
        elements = line.split(' ')
        for i in elements[:-1]:
            if(parola == i):
                cont += 1

    print(f"Numero di ricorrenze di {parola} = {cont}")
    my_file.close()
    
#Funzione che preso un file crea un dizionario con quante volta c'è una parola (chiave)
def fileToDict():
    wordDict = {}
    my_file = open('test.txt', 'r')
    for line in my_file:
        elements = line.split(' ')
        for i in elements[:-1]:
            if(i in wordDict):
                wordDict[i] +=1
            else:
                wordDict[i] = 1
        
    for chiave, valore in wordDict.items():
        print(f"{chiave}: {valore}")
    my_file.close()

#Funzione che preso un file e rimuove tutte le righe duplicate
def createUnique():
    values = []
    my_file = open('test.txt', 'r')
    my_file2 = open('unique.txt', 'x')
    
    for line in my_file:
        if not (line in values):
            my_file2.write(line)
            values.append(line)

    my_file.close()
    my_file2.close()


createUnique()