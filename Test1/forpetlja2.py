while True:
    broj = int(input("Unesi cijeli broj: "))
    if broj > 0 and broj % 8 == 0:
        print("Unio si pozitivan broj djeljiv sa 8:", broj)
        break
    else:
        print("Broj nije pozitivan i/ili nije djeljiv sa 8. Pokušaj ponovo.")