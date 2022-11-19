import random

punkty = [round(random.uniform(0,50),2) for i in range(15)]
print(punkty)

print(f"Najwięcej zdobytych punktów: {max(punkty)}, najmniej zdobytych punktów: {min(punkty)}")

liczba = float(input("Podaj liczbę punktów :"))

if liczba in punkty:
     print(punkty.index(liczba))
else:
    print("Liczba nie występuje w liście PUNKTY")

suma = sum(punkty)

srednia = suma/len(punkty)

print(f"Średnia punktów: {srednia}")

punkty_powyżej = []

for i in punkty:
    if i > srednia:
        punkty.append(i)
    else:
        punkty.append(i)

print(f'ile osób uzyskało powyżej średniej {srednia}: {len(punkty_powyżej)}')
print(f'ile osób uzyskało poniżej średniej {srednia}: {len(punkty_poniżej)}')