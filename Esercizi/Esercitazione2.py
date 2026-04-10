class ExamException(Exception):
    pass


class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        try:
            my_file = open(self.name,"r")
            superList = [] #Questa è la mia lista di liste

            previous_year = -9999 #Questo mi assicura che va bene l'anno sempre
            previous_month = -9999 #Questo mi assicura che va bene qualunque mese
            for linea in my_file:
                elementi = linea.split(",")
                if(len(elementi)>=2):#Esclude le righe con 1 solo elemento, perchè in quel caso sarà sicuramente sbagliato
                    try:
                        elementi[1] = int(elementi[1]) #Se il secondo elemento non può essere convertito in un intero, allora l'elemento sicuramente non c'è e viene gestito dall'except

                        #Controllo Ulteriore per vedere se è valido l'elemento 1
                        date = elementi[0].split("-")
                        if(len(date) == 2):#Esclude le righe che non sono in formato "x-y"
                            #convertendo queste righe in int, allora posso confermare che sono date (non al 100%, perchè potrebbe non essere nel formato YYYY-mm)
                            date[0] = int(date[0])
                            date[1] = int(date[1])

                            if(date[0] > previous_year):
                                previous_year = date[0]
                                previous_month = date[1]
                                actualElement = [] #Senno aggiunge anche elementi che sono in più
                                actualElement.append(elementi[0])
                                actualElement.append(elementi[1])
                                superList.append(actualElement)
                            elif(date[0] == previous_year):
                                if(date[1] > previous_month):
                                    if(elementi[1]>0):
                                        previous_year = date[0]
                                        previous_month = date[1]
                                        actualElement = [] #Senno aggiunge anche elementi che sono in più
                                        actualElement.append(elementi[0])
                                        actualElement.append(elementi[1])
                                        superList.append(actualElement)
                                else:
                                    raise ExamException("Errore, la lista non è ordinata")
                                #Si potrebbe anche fare il controllo specifico per dire che c'è un duplicato, ma funziona anche così
                            else:
                                raise ExamException("Errore, la lista non è ordinata")


                    except ValueError:
                        print("Riga Non valida")
                    

            return superList
        except IOError:
            raise ExamException("Errore, C'è un errore non è leggibile")
        except FileNotFoundError:
            raise ExamException("Errore, File non esiste")
        except PermissionError:
            raise ExamException("Errore, Non si può accedere al file")
        
def compute_variations(lista, firstYear,lastYear):
    try:
        firstYear = int(firstYear)
        lastYear = int(lastYear)
        
    except ValueError:
        raise ExamException("Errore: valori passati errati")    
    #La lista ottenuta da getData è gia ordinata, quindi posso cercare il primo indice in cui compare 
    i=0
    elementi = lista[i][0].split("-")
    while(int(elementi[0])<firstYear):
        i = i+1
        elementi = lista[i][0].split("-")
    
    minYearIndex = i
    if(int(lista[minYearIndex][0].split("-")[0]) != firstYear):
        raise ExamException("Non c'è first year")    

    while(int(elementi[0])<lastYear+1):
        i = i+1
        elementi = lista[i][0].split("-")
    
    maxYearIndex = i
    #Questo mi da l'indice dell'elemento dopo all'ultimo elemento che ha anno lastyear
    if(int(lista[maxYearIndex-1][0].split("-")[0]) != lastYear):
        raise ExamException("Non c'è last year") 

    my_dict = {}
    valore = 0
    contatore = 0
    previousYearRange = -1
    thisYear = int(lista[minYearIndex][0].split("-")[0])
    for i in range(minYearIndex,maxYearIndex):
        if(int(lista[i][0].split("-")[0]) == thisYear):
            contatore = contatore+1
            valore = valore +  int(lista[i][1])
        else:
            if(previousYearRange != -1):
                my_dict[f"{thisYear-1}-{int(lista[i][0].split("-")[0])-1}"] = (valore/contatore) - previousYearRange
            
            previousYearRange = valore/contatore
            contatore = 1
            valore = int(lista[i][1])
            thisYear = int(lista[i][0].split("-")[0])

    my_dict[f"{thisYear-1}-{thisYear}"] = (valore/contatore)-previousYearRange


    
    return my_dict
        



time_series_file = CSVTimeSeriesFile("data.csv")
time_series = time_series_file.get_data()

dizionario = compute_variations(time_series,"1949","1952")
for chiave, valore in dizionario.items():
    print(chiave, valore)