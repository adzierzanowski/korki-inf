# Słownik - struktura danych, która przechowuje pary klucz-wartość
# Klucze nie muszą być stringami, wartości nie muszą być intami
slownik = {'a': 1, 'b': 2, 'c': 3}

# Aby dostać się do wartości z klucza, używamy nawiasów kwadratowych
print(slownik['a']) # = 1

# Aby dodać nowy element do słownika, używamy nawiasów kwadratowych
slownik['d'] = 4

# Aby usunąć element z słownika, używamy słowa kluczowego del
del slownik['b']

# Aby sprawdzić czy dany klucz jest w słowniku, używamy słowa kluczowego in
print('a' in slownik) # = True
print('b' in slownik) # = False (bo usunęliśmy)

# Iterowanie po słowniku
# Możemy iterować po kluczach, wartościach lub parach klucz-wartość
for klucz in slownik:
  print(klucz) # a, c, d

for wartosc in slownik.values():
  print(wartosc) # 1, 3, 4

for klucz, wartosc in slownik.items():
  print(klucz, wartosc) # a 1, c 3, d 4

# Dict comprehension
# ==================
# Słowniki możemy definiować podobnie do list comprehension
slownik = {napis: len(napis) for napis in ['a', 'bbb', 'ccccc', 'ddddd', 'eeee']}
#          ^^^^^  ^^^^^^^^^^     ^^^^^    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#          klucz  wartość        |                                        |
#                                |zmienna reprezentująca                  |
#                                element bazowego kontenera               |
#                                                                     bazowy kontener
