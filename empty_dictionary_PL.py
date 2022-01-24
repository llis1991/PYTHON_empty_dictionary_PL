definicje = {}
while 0<1:
    print("1 - dodaj definicje")
    print("2 - szukaj definicji")
    print("3 - usuń definicję")
    print("4 - zakończ program")
    chose = input("co chcesz zrobić?")
    if (chose=='1'):
        haslo  = input("podaj hasło do zdefiniowania: ")
        definicja = input("podaj definicję: ")
        definicje.update({haslo: definicja})
    elif (chose=='2'):
        szukaneHaslo = input("jakiego hasła szukasz? ")
        if (szukaneHaslo in definicje):
            print("definicja dla",szukaneHaslo,"to:",definicje[szukaneHaslo])
        else:
            print("nie ma takiego hasła")
    elif (chose=='3'):
        doUsuniecia = input("jakie hasło chcesz usunać? ")
        if (doUsuniecia in definicje):
            del (definicje[doUsuniecia])
        else:
            print("nie ma takiego hasła")
    elif (chose=='4'):
        break
        
        
    
     
