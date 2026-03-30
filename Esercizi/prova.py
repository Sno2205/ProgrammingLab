lista = [1,1,2,2,3,3,4,5]
max = 5

i = 0
while(i<len(lista) and lista[i]<max+1):
    print(f"Controllo {i} = {lista[i]}<{max}")
    i = i+1

print(i)
