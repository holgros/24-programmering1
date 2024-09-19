# EN LISTA KAN INNEHÅLLA ELEMENT AV FLERA OLIKA DATATYPER
lista = [11, 2, 6, 8, 12, 3] # lista med heltal
#lista = list("ett", False, 2.0, 2) # lista med flera datatyper
lista = [] # en tom lista

# ÅTKOMST AV ELEMENT VIA INDEX
lista = [11, 2, 6, 8, 12, 3]
element = lista[0] # läser värdet på plats 0
print(element)  # skriver ut 11
print(lista) # skriver ut [11, 2, 6, 8, 12, 3]
lista[0] = "hej" # ändrar värdet på position 0
print(lista) # skriver ut [“hej”, 2, 6, 8, 12, 3]

# NEGATIVA INDEX
lista = [11, 2, 6, 8, 12, 3]
element = lista[-1]
print(element)  # Skriver ut 3

# LÄGGA TILL ELEMENT MED METODEN APPEND
lista = [1, 2, 3]
lista.append(42) # append lägger på ett element på slutet
print(lista) # skriver ut [1, 2, 3, 42]

# TA BORT ELEMENT MED METODEN POP
lista = [1, 2, 3]
# pop() tar bort det sista elementet och returnerar det
element = lista.pop()
print(element) # skriver ut 3
print(lista) # skriver ut [1, 2]
lista = [1, 2, 3]
# pop(index) tar bort elementet med det angivna indexet 
# och returnerar det
element = lista.pop(1)
print(element)  # skriver ut 2
print(lista)  # skriver ut [1, 3]

# FUNKTIONEN RANGE
lista = list(range(5))
print(lista) # skriver ut [0, 1, 2, 3, 4]

# LOOPA IGENOM EN LISTA
lista = ["ett", False, 2.0, 2]  
for x in lista:
    print(x)

# LISTA MED LISTOR
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]
lst = [lst_1, lst_2, lst_3]
print(lst)
borttagen_lista = lst.pop()
print(borttagen_lista)
print(lst)