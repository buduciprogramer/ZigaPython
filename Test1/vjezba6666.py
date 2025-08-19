def suma(lista):
    zbir = 0
    for broj in lista:
        zbir += broj
    return zbir

print("Unesite 4 elementa liste:")
moja_lista = []
for i in range(4):
    broj = int(input())
    moja_lista.append(broj)

rezultat = suma(moja_lista)
print("Suma elemenata je:", rezultat)