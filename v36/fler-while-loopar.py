#
#   while-loopar används när man vill loopa så länge något är sant.
#   Det kan bli oändligt om man inte passar sig!
#

# Ex: while loop som körs så länge varabeln i är mindre än 6
# skriver ut värdet på variabeln i och räknar upp värdet med 1.
i = 1
while i < 6:
    # allt som är "intabbat" här görs varje varv i loopen
    print(i)
    i = i + 1

# Ex: while-loop som körs så länge i är större än 0.
# Skriver ut lika många bindestreck som värdet i variabeln i.
# Minskar värdet på i med 1.
i = 10
while i > 0:
    print("-"*i)
    i -= 1


# Ex. avsluta en loop inifrån kodblocket med hjälp av "break".
i = 1
divider = 10
while i < 100:
    print(i)
    if i % divider == 0:
        break  # break gör att loopen stoppas och programmet fortsätter med kod efter loopen
    i = i + 1

print(f"i har värdet {i} efter loopen")  # den här körs efter loopen
