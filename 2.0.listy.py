# Lista - lista elementów, które mogą być różnych typów
lista = [1, 2, 3, 'a', 'b', 'c']

# Przydatne metody listy
# ======================

lista.append('element') # Dodaje element do listy
lista.remove('element') # Usuwa konkretny element listy
ostatni = lista.pop()   # Usuwa ostatni element listy i go zwraca (odwrotność append)
lista.count(1)          # Zwraca liczbę elementów równych pierwszemu argumentowi
lista.index(1)          # Zwraca pierwszą pozycję, na której występuje dany element
#lista.sort()            # Sortuje listę (można podać jako argument key=f,
                        #                gdzie f to funkcja, która zwraca obiekt,
                        #                po którym odbywa się sortowanie)
#lista2 = sorted(lista)  # Działa jak powyżej, tylko zamiast modyfikować listę,
                        #     to zwraca nową
len(lista)              # Zwraca długość listy

# Sortowanie z kluczem
# ====================
# Funkcja sorted i metoda sort przyjmują opcjonalny argument key, który
# wskazuje, co ma być sortowane. Lista może się przecież składać ze skomplikowanych
# obiektów, więc nie zawsze odpowiada nam domyślne sortowanie, a czasem jest
# wręcz niemożliwe.
#
# Np. mamy listę punktów:
punkty = [(0,0), (7,16), (8,2), (1,1), (9,3)]

# Chcemy ją posortować wg odległości od punktu (0, 0)
# Jak wiadomo, odległość ta może być dana wzorem np. |x| + |y|
# Wtedy definiujemy funkcję, która powie metodzie sortującej, żeby sortowała
# po wyniku działania funkcji na danym elemencie, a nie po samym elemencie.

def sortuj_po(element):
  x, y = element
  return abs(x) + abs(y)

print(sorted(punkty, key=sortuj_po)) # [(0, 0), (1, 1), (8, 2), (9, 3), (7, 16)]

# Co daje nam inny wynik niż domyślne sortowanie par liczb, gdzie najpierw
# porównywany jest pierwszy element, a potem drugi

print(sorted(punkty)) # [(0, 0), (1, 1), (7, 16), (8, 2), (9, 3)]

# Możemy tę funkcję napisać zwięźlej używając funkcji anonimowej (bez nazwy)
# czyli lambdy
print(sorted(punkty, key=lambda element: abs(element[0]) + abs(element[1])))

# Lambdy składają się ze słowa lambda, listy argumentów, dwukropka i zwracanej wartości

lambda x, y: x + y

# jest równoważna (poza tym, że nie ma ona nazwy)

def funkcja(x, y):
  return x + y

# List comprehension - składnia do tworzenia list
# ===============================================
# Przykładowo:
lista = [x // 2 for x in range(10)]
#        ^^^^^^     ^    ^^^^^^^^^
#          |        |     Bazowa lista (bądź inna struktura danych)
#     wzór na       |
# wynikowy element  |
#                   zmienna reprezentująca
#                   element bazowego zbioru

# Oczywiście nie muszą być to wzory matematyczne
# równie dobrze możemy przekształcać elementy listy poprzez użycie zaawansowanych funkcji

# Przykładowo mamy listę stringów, a chcemy zrobić z nich listę liczb całkowitych
lista = ['1', '2', '3', '4', '5']
lista = [int(x) for x in lista]
# czyli:
# for x in lista -- dla każdego x w liście lista
# int(x)         -- tworzymy nową listę zawierającą elementy przekonwertowane na int

# Możemy również ograniczyć (filtrować) listę do elementów spełniających pewien warunek
# Przykładowo chcemy otrzymać listę liczb podzielnych przez 7 z zakresu 0-49
lista = [x for x in range(50) if x % 7 == 0]

# Albo wybrać tylko te napisy z listy, które mają co najmniej 3 litery 'a'
lista = ['akacja', 'abażur', 'ananas', 'arbitraż', 'arbuz', 'abstrakcja']
lista = [napis for napis in lista if napis.count('a') >= 3]

# I ostatni przykład. Chcemy otrzymać listę obiektów klasy Point o współrzędnych z listy
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # Odległość punktu od początku układu współrzędnych
  def length(self):
    return (self.x ** 2 + self.y ** 2) ** 0.5

wspolrzedne = [(1, 1), (22, 10), (3.3, 1.1), (4, 8), (3, 5), (12, 16)]
punkty = [Point(x, y) for x, y in wspolrzedne]
dlugosci = [punkt.length() for punkt in punkty]
