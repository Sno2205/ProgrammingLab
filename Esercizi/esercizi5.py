from classi import Veicolo
def CreaLista(n):
    list = []
    for i in range(n):
        elemento = input(f"Dammi il {i+1} elemento!!\n")
        list.append(elemento)
    return list

class Persona:
    def __init__(self, titolo, nome, cognome):
        self.titolo = titolo
        self.nome = nome
        self.cognome = cognome
        
    def saluta(self):
        print(f"{self.titolo} {self.nome} {self.cognome}")
  
class Studente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Studente", nome, cognome)
        self.corsi = corsi
        
    def saluta(self):
        super().saluta()
        stringa = ""
        for corso in self.corsi:
            stringa += corso.strip() + "\t"
        print(f"Frequenta il corso: {stringa}")

    def controlloProfessori(self,docentiList):
        listaProf = []
        i=1
        for docente in docentiList:
            if(docente.controlloStudente(self)):
                stringa = f"{i})" + docente.nome + docente.cognome
                listaProf.append(stringa)
            i+=1
        return listaProf

    
class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi

    def saluta(self):
        Persona.saluta(self)
        stringa = ""
        for corso in self.corsi:
            stringa += corso.strip()  + "\t"

        print("> Docente dei corsi di: ", stringa)
    
    def controlloStudente(self,studente):
        ctrl = True
        for corso in self.corsi:
            if not (corso in studente.corsi):
                ctrl = False
            
        return ctrl

class Auto(Veicolo):
    def __init__(self, modello, marca, anno, nPorte):
        super().__init__(modello, marca, anno)
        self.nPorte = nPorte
    
    def __str__(self):
        return super().__str__() +  f" e numero porte = {self.nPorte}"

class Moto(Veicolo):
    def __init__(self, modello, marca, anno, tipo):
        super().__init__(modello, marca, anno)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + f"tipo = {self.tipo}"


def menu():
    studentList = []
    docentiList = []
    scelta = 1
    while scelta != 0:
        print("\n=== MENU PRINCIPALE ===")
        print("1. Aggiungi Studente")
        print("2. Aggiungi Professore")
        print("3. Controllo Studenti")
        print("4. Dato uno studente controlla se c'è un prof che insegna tutte le materie")
        print("0. Esci")
        
        try:
            scelta = int(input("Scegli un'opzione: "))
            
            match scelta:
                case 0:
                    print("Uscita dal programma...")
                case 1:
                    nome = input("Nome")
                    cognome = input("Cognome")
                    lista = CreaLista(4)
                    s = Studente(nome, cognome, lista)
                    studentList.append(s)
                case 2:
                    nome = input("Nome")
                    cognome = input("Cognome")
                    lista = CreaLista(4)
                    s = Docente(nome, cognome, lista)
                    docentiList.append(s)
                case 3:
                    printare = "Lista Docenti: \n"
                    i = 1
                    for docente in docentiList:
                        printare += f"{i}" + docente.nome + docente.cognome + "\n"
                        i+=1
                    
                    printare += "\n Lista Studenti: \n"
                    i = 1
                    for studente in studentList:
                        printare += f"{i}" + studente.nome + studente.cognome + "\n"
                        i+=1
                    
                    print(printare)
                    iDoc = int(input("Inserisci indice Docente"))
                    iStud = int(input("Inserisci indice Studente"))
                    ctrl = docentiList[iDoc-1].controlloStudente(studentList[iStud-1])
                    print(ctrl)
                case 4:
                    printare = "Lista Studenti: \n"
                    i = 1
                    for studente in studentList:
                        printare += f"{i}" + studente.nome + studente.cognome + "\n"
                        i+=1
                    
                    print(printare)
                    iStud = int(input("Inserisci indice Studente"))
                    listaProf = studentList[iStud-1].controlloProfessori(docentiList)

                    for Prof in listaProf:
                        print(Prof)
                case _:
                    print("Opzione non valida! Scegli tra 0-3")
                    
        except ValueError:
            print("Inserisci un numero valido!")

class Poligono():
    def __init__(self, nLati):
        self.nLati = nLati
    
    def __str__(self):
        return f"Sono un poligono di {self.nLati} lati"
    

class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)
    
    def __str__(self):
        return "Sono un quadrilatero"

class Rettangolo(Quadrilatero):
    def __init__(self, base, altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def __str__(self):
        return f"Sono un Rettangolo con base = {self.base} e altezza = {self.altezza}"
    
    def perimetro(self):
        return self.base*2 + self.altezza*2
    
    def area(self):
        return self.base*self.altezza
    

class Triangolo(Poligono):
    def __init__(self, lato1,lato2,lato3):
        super().__init__(3)
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3
    
    def __str__(self):
        return f"Sono un Triangolo con lato 1 = {self.lato1}, lato 2 = {self.lato2} e lato 3 = {self.lato3}"
    
    def Perimetro(self):
        return self.lato1+self.lato2+self.lato3
    
    def is_equilatero(self):
        if(self.lato1 == self.lato2 and self.lato2 == self.lato3):
            return True
        else:
            return False
        

print("dio cane")
p = Poligono(6)
print(p)
t1 = Triangolo(1,2,3)
print(t1)
print(t1.is_equilatero())
print(t1.Perimetro())
t1 = Triangolo(3,3,3)
print(t1)
print(t1.is_equilatero())
print(t1.Perimetro())
q = Quadrilatero()
print(q)
r = Rettangolo(1,2)
print(r)
print(r.perimetro())
print(r.area())