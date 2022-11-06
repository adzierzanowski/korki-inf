# Python ma mnóstwo tzw. lukru składniowego, czyli składni, która nie jest
# wymagana, ale ułatwia życie programiście oferując zwięzły zapis na skomplikowane
# operacje. Przykładem jest list comprehension, którego używamy do tworzenia list,
# ale nie tylko.


# ZAMIANA DWÓCH ZMIENNYCH
# =======================
# Chcemy zamienić wartości a i b ze sobą
a = 1
b = 2

# Zwykły sposób wymaga zastosowania dodatkowej zmiennej
tmp = a
a = b
b = tmp

# W Pythonie można to zrobić w jednej linijce
a, b = b, a


# F-STRINGI (od Pythona 3.6)
# ==========================
# pozwalają na łatwe formatowanie napisów
# Sczególnie przydatne przy tworzeniu napisów złożonych z wielu zmiennych
print(f'a = {a}, b = {b}')


# ROZPAKOWYWANIE KROTEK/LIST
# ==========================
# Funkcje takie jak np. print przyjmują dowolną liczbę argumentów, a każdy
# z nich domyślnie oddzielany jest spacją
print('wartość a:', a)

# Powiedzmy, że chcemy wypisać elementy jakiejś listy
lista = [1, 2, 3, 4, 5]

# Normalnie musielibyśmy pisać
print('Elementy listy:', lista[0], lista[1], lista[2], lista[3], lista[4])

# Ale możemy skorzystać z rozpakowywania listy
# czyli zamiany listy na kolejne argumenty funkcji
print('Elementy listy:', *lista)

# Rozpakowywanie przydaje się również przy tworzeniu zmiennych
lista = [1, 2, 3, 4, 5]
jeden, dwa, *reszta = lista # jeden=1, dwa=2, reszta=[3, 4, 5]


# ODWRACANIE LISTY
# ================
odwrocona = lista[::-1]
