from esercizi4 import CSVFile
from datetime import *

class NumericalCSVFile(CSVFile):
    def __init__(self,name):
        super().__init__(name)
        
    def get_data(self,*args, **kwargs):
        listaShampo = super().get_data(*args, **kwargs)
        for shampoo in listaShampo:
            try:
                shampoo[1] = float(shampoo[1])
            except ValueError:
                print("Ci sono errori nel file")
        return listaShampo
    
def prossimoCompleanno(dataNascita):
    now = date.today()
    compl = datetime.strptime(dataNascita, "%Y-%m-%d")
    year = now.year
    if(compl.month < now.month):
        year = year + 1
    elif(compl.month == now.month):
        if(compl.day <= now.day):
            year = year + 1

    next_compl = datetime.strptime(f"{year}-{compl.month}-{compl.day} 00:00:00", "%Y-%m-%d %H:%M:%S")

    return next_compl-datetime.now()

def Quadrato(numero):
    return numero*numero

def somma(numero1, numero2):
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        return numero1+numero2
    except (ValueError,TypeError):
        print("Valori non validi")
        return 0
    
    

def differenza(numero1, numero2):
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
    except (ValueError,TypeError):
        print("Valori non validi")
    
    return numero1-numero2


"""
csv = NumericalCSVFile("shampoo_sales.csv")
list = csv.get_data(4,4)
for item1 in list:
    for item2 in item1:
        print(f"{item2}")
    print("\n")
"""


#Esercizio 5
#dataNascita = input("Dammi la tua data di Nascita in formato 2024-03-30 (YYYY-MM-DD)")
#Non ho voglia di scriverlo

"""
dataNascita = "2004-04-03"
print(prossimoCompleanno(dataNascita))
"""

#Esercizio 6
"""
flag = True
while(flag):
    try:
        numero = int(input("Inserisci Numero Intero"))
        flag = False
    except ValueError:
        print("Devi Inserire un numero intero")

print(Quadrato(numero))
"""

#Esercizio 7
ctrl = 1
while(ctrl != 3):
    print("\n--- MENU ---")
    print("1. Calcolare la somma di due numeri")
    print("2. Calcolare la differenza tra due numeri")
    print("3. Uscire")
    
    try:
        ctrl = int(input("Scegli un'opzione (1-3): "))
    except ValueError:
        ctrl = 4 #è un valore che non è nel menu quindi dira valore non valido

    match ctrl:
        case 1:
            num1 = input("Inserisci il primo numero: ")
            num2 = input("Inserisci il secondo numero: ")
            risultato = somma(num1, num2)
            print(f"La somma di {num1} e {num2} è: {risultato}")
                
        case 2:
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
            risultato = differenza(num1, num2)
            print(f"La differenza tra {num1} e {num2} è: {risultato}") 
        case 3:
            print("Uscita dal programma. Arrivederci!")
            
        case _:
            print("Opzione non valida. Scegli tra 1, 2 o 3.")




