import random
n=int(input("podaj długość listy: "))
zestaw_1 = []
i = random.randint(1,10)
zestaw_1.append(i)
for i in range(n):
    k = random.randint(1, 10)
    zestaw_1.append(k)
print(zestaw_1)
import random
n=int (input("PODAJ LICZBE:"))
lista_1 = []
for x in range(n):
    k  = random.randint(1, 10)
    lista_1.append(k)
print(lista_1)
n=int(input("Podaj dlugosc listy:"))
zestaw_2 = [random.randint(5,15) for i in range(n)]
print(zestaw_2)
liczba = int(input("podaj liczbę"))
if liczba in zestaw_1:
    print('liczba występujące w zestawie 1')
elif liczba in zestaw_2:
    print ('liczba występuje w zestawie 2')
else:
    print ('liczba nie występuje w obu zestawach')

zestaw_3 = zestaw_1+zestaw_2

print(zestaw_3)
zestaw_3.sort()
print(zestaw_3)


