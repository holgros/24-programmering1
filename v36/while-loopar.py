# En enkel while-loop
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1  # i ökar med 1
print(f"\nProgrammet avslutas eftersom i = {i}")

# Detta program beräknar summan av ett antal tal
avsluta = False
summa = 0
while not avsluta:
    tal = int(input("Ange ett valfritt tal, noll avslutar -> "))
    if tal == 0:
        avsluta = True
    summa += tal
print(f"Summan är {summa}")

# Samma program som ovan, men med kommandot "break"
# Detta program beräknar summan av ett antal tal
summa = 0
while True:
    tal = int(input("Ange ett valfritt tal, noll avslutar -> "))
    if tal == 0:
        break       # OBS: gör att loopen avslutas  och går direkt till rad 26
    summa += tal
print(f"Summan är {summa}")


# Detta program beräknar summan av ett antal positiva tal
summa = 0
while True:
    tal = int(input("Ange ett valfritt tal, noll avslutar -> "))
    if tal == 0:
        break       # OBS: gör att loopen avslutas  och går direkt till rad 38
    if tal < 0:
        continue    # OBS: gör att loopen går tillbaka till rad 31 igen
    summa += tal
print(f"Summan av de inmatade positiva talen är {summa}")

# Detta program demonstrerar nästlade loopar
i = 0
while i < 3: # Start yttre loop
    j = 0
    while j < 3: # Start inre loop
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1
print("Programmet avslutas")