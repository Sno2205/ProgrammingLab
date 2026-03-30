from esercizi4 import CSVFile

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
    

csv = NumericalCSVFile("shampoo_sales.csv")
list = csv.get_data(4,4)
for item1 in list:
    for item2 in item1:
        print(f"{item2}")
    print("\n")
    




