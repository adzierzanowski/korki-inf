# Tuple - krotka, czyli lista niezmienialna

# Większość rzeczy dot. list odnosi się również do krotek
# Żeby przekonwertować listę na krotkę:
#   krotka = tuple(lista)

krotka = (1, 2, 3, 'a', 'b', 'c')
try:
  krotka[0] = 2 # Błąd, krotka jest niezmienialna; z listą takiego błędu nie ma
except TypeError:
  print('Nie można zmienić elementu krotki')

# Po co nam niezmienialna lista?
# Krotki zużywają mniej pamięci niż listy, więc są szybsze
# Jeżeli wiemy, że nasza lista nie będzie się zmieniać, to warto użyć krotki
