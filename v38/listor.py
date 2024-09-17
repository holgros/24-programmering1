# SKAPA EN LISTA OCH LÄSA VÄRDEN FRÅN LISTAN
temperaturer = [10, 12, 8, 9, 7] # EN variabel för FEM temperaturer
print(temperaturer[0])  # 10
print(temperaturer[2])  # 8

# SKAPA EN TOM LISTA OCH LÄGGA TILL ELEMENT
scores = []         # Skapar en tom lista
scores.append(42)   # Lägger till talet 42 i den från början tomma listan
scores.append(50)   # Lägger till talet 50 sist i listan
print(scores[0])    # 42
print(scores[1])    # 50

# SKAPA EN LISTA MED FUNKTIONEN RANGE
lst = list(range(-4, 6, 3))
print(lst)