def creaLista(n):
    lista = []
    i = 0
    while(i<n):
        try:
            valore = int(input("Inserisci valore nella lista: "))
            lista.append(valore)
            i = i+1
        except ValueError:
            print("DEVI INSERIRE VALORI VALIDI")
        
    
    return lista

class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, lun):
        if(isinstance(lun, int)):
            self.lun = lun
        else:
            raise ExamException("Errore, non è un intero")
    
    def compute(self, lista):
        if(isinstance(lista, list)):
            if(len(lista)>=self.lun):
                listaFinMobile = []
                min_iter = 0
                max_iter = self.lun
                
                while(max_iter<=len(lista)):
                    somma = 0
                    for i in range(min_iter,max_iter):
                        if(isinstance(lista[i],int)):
                            somma = somma + lista[i]
                        else:
                            raise ExamException("Errore, la lista non contiene solo interi")
                    
                    media = somma/self.lun
                    listaFinMobile.append(media)
                    max_iter = max_iter+1
                    min_iter = min_iter+1
            
                return listaFinMobile
                    
            else:
                raise ExamException("Errore, Ci sono troppo pochi elementi nella lista")
        else:
            raise ExamException("Errore, lista valori vuota")
        return []
    

boh = MovingAverage(2)

lista = creaLista(1)
print("Lista Utente")
for i in lista:
    print(i)

print("Lista Risultati")
result = boh.compute(lista)
for i in result:
    print(i)