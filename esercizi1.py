#Funzione minuti in ora con input dentro alla funzione
def ConversioneMinToHour():
    minTot  = int(input("Quanti minuti sono??"))
    hour = int(minTot/60)
    min = minTot%60
    print(f"{minTot} minuti sono {hour} ore e {min} minuti")


#Funzione Quadrato e Cubo con input dentro alla funzione
def QuadratoCubo():
    numero = int(input("Dammi un numero!!"))
    quadrato = numero ** 2
    cubo = numero ** 3
    print(f"Quadrato = {quadrato}\n Cubo = {cubo}")

#Funzione Che dice se un numero è pari o dispari con input dentro alla funzione  
def PariDispari():
    numero = int(input("Dammi un numero!!"))
    if(numero%2 == 0):
        print("Numero pari")
    else:
        print("Numero dispari")

#Funzione che conta le ripetizione di una lettera in una parola con input dentro alla funzione  
def contaRipetizioni():
    lettera = input("Dammi un lettera!!")
    parola = input("Dammi un parola!!")

    contatore = 0
    for i in parola:
        if(lettera == i):
            contatore +=1
        
    print(f"La lettera {lettera} è ripetuta {contatore} volte in {parola}")

#Funzione che dice se un numero è primo con input dentro alla funzione  
def isPrime():
    numero = int(input("Dammi un numero!!"))
    flag = True
    for i in range (2, numero):
        if(numero%i == 0):
            flag = False
    if flag:
        print("Numero Primo")
    else:
        print("Numero non Primo")


#Funzione che somma i numeri finchè non gli si dice stop digitando 0
def sommaSemiInf():
    flag = True
    somma = 0
    n = 0
    while flag:
        numero = int(input("Dammi un numero!!"))
        if(numero == 0):
            flag = False
        else:
            somma += numero
            n+=1

    print(f"La somma dei {n} elementi è {somma}")


#Funzione Fattoriale
def fattoriale():
    numero = int(input("Dammi un numero!!"))
    prod = 1
    for i in range(2,numero+1):
        prod *= i

    print(f"Il fattoriale di {numero} è {prod}")

#Vede se 3 lati possono fare un triangolo
def PossibileTriangolo(a,b,c):
    return a + b > c and a + c > b and b + c > a

#Funzione per vedere se 3 lati possono fare un triangolo con input dentro la funzione
def IdentificaTriangolo():
    lato1 = int(input("Dammi un numero!!"))
    lato2 = int(input("Dammi un numero!!"))
    lato3 = int(input("Dammi un numero!!"))
    flag = PossibileTriangolo(lato1,lato2,lato3)
    print(f"{flag}")

    if(not flag):
        print("No triangolo")
    elif(lato1 == lato2 == lato3):
        print("Triangolo Equilatero")
    elif(lato1 == lato2 or lato2 == lato3 or lato1 == lato3):
        print("Triangolo Isoscele")
    else:
        print("Triangolo scaleno")


#Funzione che conta il numero di vocali in una stringa
def contaVocali():
    vocali = "aeiou"
    cont = 0
    parola = input("Dammi un parola!!")
    for i in parola:
        if(i in vocali):
            cont +=1

    print(f"In {parola} ci sono {cont} vocali")