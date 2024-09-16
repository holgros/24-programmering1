# loopa igenom en lista
lista = [10, 20, 30]
for element in lista:
    print(element, end=" ")
print(f"Loopen avslutas eftersom listan är slut")

# funktionen range
for i in range(3, 8):   # Här skapas listan
    print(i, end=" ")
print()                 # radbrytning

# range kan ta emot 1, 2 eller 3 argument
lista_A = list(range(10))       # samma som range(0, 10)
lista_B = list(range(-5, 5))    # starta med negativt tal
lista_C = list(range(0, 10, 2)) # två steg i taget
lista_D = list(range(10, 0, -1))    # stega baklänges
print(f"lista_A = {lista_A}")   # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(f"lista_B = {lista_B}")   # -5, -4, -3, -2, -1, 0, 1, 2, 3, 4
print(f"lista_C = {lista_C}")   # 0, 2, 4, 6, 8
print(f"lista_D = {lista_D}")   # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Detta program beräknar och skriver ut "tolvans tabell"
for i in range(1, 13):
    print(f"{i:2.0f} * 12 = {i*12:3.0f}")

# en lista kan även innehålla textsträngar (inte bara heltal)
items = ["Klocka", "Kikare", "Termometer"]
print("Du har tillgång till:", end=" ")
for item in items:
    print(item, end=" ")