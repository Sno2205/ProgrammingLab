import random

class Coin():

    def __init__(self):
        self.faccia = None
    
    def __str__(self):
        return f"La faccia è {self.faccia}"

    def lanciaMoneta(self):
        if(random.randint(0,1) == 0):
            self.faccia = "testa"
        else:
            self.faccia = "croce"


class Veicolo():
    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0
    
    def __str__(self):
        return f"Veicolo {self.marca} {self.modello} del {self.anno} con velocità di {self.speed} km/h"
    
    def accellerare(self):
        self.speed += 5
    
    def frenare(self):
        if(self.speed != 0):
            self.speed -= 5
        
    def get_speed(self):
        return self.speed
if __name__ == '__main__':
    ctrl = True
    veicolo = Veicolo("Boh", "Boh", 2000)
    while ctrl:
        print("\n=== MENU PRINCIPALE ===")
        print("1. Saluta")
        print("2. Mostra data e ora")
        print("3. Calcola quadrato")
        print("4. Esci")
        
        scelta = input("Scegli un'opzione (1-4): ")
        
        match scelta:
            case "1":
                veicolo.accellerare()
            case "2":
                veicolo.frenare()
            case "3":
                print(f"{veicolo.get_speed()}")
            case "4":
                print("Arrivederci!")
                ctrl = False
                
            case _:
                print("Opzione non valida! Scegli tra 1 e 4.")
