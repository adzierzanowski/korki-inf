# Set - zbiór, czyli lista unikalnych elementów
#       każdy element może wystąpić tylko raz
zbior = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) # zbiór tożsamy z {1, 2, 3, 4}
zbior.add(5)
zbior.remove(4)

# Poza tym dostępne są wszystkie operacje na zbiorach znane z matematyki
zbior1 = set([1, 2, 3, 4, 5])
zbior2 = set([4, 5, 6, 7, 8])

suma = zbior1.union(zbior2)                 # Z1 u Z2
roznica = zbior1.difference(zbior2)         # Z1 \ Z2
czesc_wspolna = zbior1.intersection(zbior2) # Z1 n Z2

# Zbiory przydają się w sytuacji, gdy mamy powtarzające się elementy,
# a interesuje nas np. tylko to, czy w ogóle wystąpiły.
