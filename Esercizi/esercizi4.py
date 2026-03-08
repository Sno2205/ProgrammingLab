class CSVFile():
    def __init__(self):
        self.name = "shampoo_sales.csv"
    
    def get_data(self):
        superList = []
        my_file = open(self.name, 'r')
        for line in my_file:
            values = []
            elements = line.split(',')
            if elements[0] != 'Date':
                #date = elements[0]
                #sales = elements[1]
                values.append(elements[0])
                values.append(elements[1])
                superList.append(values)
        return superList

csv = CSVFile()
list = csv.get_data()
for item1 in list:
    for item2 in item1:
        print(f"{item2}")
    

