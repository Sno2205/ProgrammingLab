class CSVFile():
    def __init__(self, name):
        if(isinstance(name,str)):
            self.name = name
        else:
            raise Exception("Deve essere una stringa")
    
    def get_data(self,start,end):
        superList = []
        try:
            my_file = open(self.name, 'r')
            linee = my_file.readlines()
            my_file.close()
            file_length = len(linee)
            if(file_length > end):
                file_length = end

            for i in range(start-1,file_length):
                values = []
                elements = linee[i].split(',')
                if elements[0] != 'Date':
                    #date = elements[0]
                    #sales = elements[1]
                    values.append(elements[0])
                    values.append(elements[1].strip())
                    superList.append(values)
        except FileNotFoundError:
            print(f"The file '{self.name}' was not found.")

        return superList
    

if __name__ == '__main__':
    csv = CSVFile("shampoo_sales.csv")
    list = csv.get_data()
    for item1 in list:
        for item2 in item1:
            print(f"{item2}")
        print("\n")
    

