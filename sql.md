# SQL

## SELECT FROM

`SELECT` wybiera kolumny z tabeli

```sql
-- Wszystkie kolumny z tabeli osoby
SELECT * FROM osoby;
```

| id                  | imie                | nazwisko            | plec                | wiek                | miasto              |
|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| 1                   | Jan                 | Kowalski            | M                   | 20                  | Warszawa            |
| 2                   | Anna                | Nowak               | K                   | 32                  | Kraków              |
| 3                   | Andrzej             | Pieczony            | M                   | 12                  | Tarnów              |
| 4                   | Rafał               | Wiśniewski          | M                   | 46                  | Opole               |
| 5                   | Janina              | Jankowska           | K                   | 66                  | Warszawa            |
| 6                   | Karol               | Krawczyk            | M                   | 38                  | Warszawa            |
| 7                   | Tadeusz             | Norek               | M                   | 38                  | Warszawa            |
| 8                   | Renata              | Wrzosek             | K                   | 38                  | Opole               |

```sql
SELECT
  imie,                 -- wybierz kolumnę imie
  miasto AS miejscowosc -- oraz miasto (z nazwą miejscowosc zamiast miasto)
FROM osoby;
```

| imie                | miejscowosc         |
|---------------------|---------------------|
| Jan                 | Warszawa            |
| Anna                | Kraków              |
| Andrzej             | Tarnów              |
| Rafał               | Opole               |
| Janina              | Warszawa            |
| Karol               | Warszawa            |
| Tadeusz             | Warszawa            |
| Renata              | Opole               |


## WHERE

`WHERE` ogranicza wynik do wierszy spełniających pewien warunek

Liczby porównujemy operatorami `<`, `>`, `<=`, `>=`, `=`, `<>` (nierówność)

Warunki łączymy poleceniami `AND` lub `OR`

```sql
SELECT * FROM osoby WHERE wiek > 12 AND wiek <> 38;
```

| id                  | imie                | nazwisko            | plec                | wiek                | miasto              |
|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| 1                   | Jan                 | Kowalski            | M                   | 20                  | Warszawa            |
| 2                   | Anna                | Nowak               | K                   | 32                  | Kraków              |
| 4                   | Rafał               | Wiśniewski          | M                   | 46                  | Opole               |
| 5                   | Janina              | Jankowska           | K                   | 66                  | Warszawa            |


### Porównywanie napisów

Stringi można porównać dokładnie:

```sql
SELECT * FROM osoby WHERE imie='Jan';
```

| id                  | imie                | nazwisko            | plec                | wiek                | miasto              |
|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| 1                   | Jan                 | Kowalski            | M                   | 20                  | Warszawa            |


Albo używając `LIKE`:

```sql
-- Wybierze wszystkie osoby z imieniem na literę J
SELECT * FROM osoby WHERE imie LIKE 'J*';
```

| id                  | imie                | nazwisko            | plec                | wiek                | miasto              |
|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| 1                   | Jan                 | Kowalski            | M                   | 20                  | Warszawa            |
| 5                   | Janina              | Jankowska           | K                   | 66                  | Warszawa            |


## ORDER BY

`ORDER BY` sortuje wiersze tabeli wg danych kolumn.

```sql
SELECT * FROM osoby ORDER BY wiek;
```

| Imie               | Nazwisko           | Plec               | Wiek              | Miasto |
|--------------------|--------------------|--------------------|-------------------|---------|
| Andrzej            | Pieczony           | M                  | **12**                |  Tarnów |
| Jan                | Kowalski           | M                  | **20**                |  Warszawa |
| Anna               | Nowak              | K                  | **32**                |  Kraków |
| Rafał              | Wiśniewski         | M                  | **46**                |  Opole |
| Janina             | Jankowska          | K                  | **66**                |  Warszawa |


### Sortowanie wg wielu kolumn

Wiersze najpierw zostaną posortowane wg płci, a potem w obrębie danej płci - wg wieku:

```sql
SELECT * FROM osoby ORDER BY plec, wiek;
```

| Imie                | Nazwisko            | Plec                | Wiek                | Miasto              |
|---------------------|---------------------|---------------------|---------------------|---------------------|
| Anna                | Nowak               | K                   | 32                  | Kraków              |
| Janina              | Jankowska           | K                   | 66                  | Warszawa            |
| Andrzej             | Pieczony            | M                   | 12                  | Tarnów              |
| Jan                 | Kowalski            | M                   | 20                  | Warszawa            |
| Rafał               | Wiśniewski          | M                   | 46                  | Opole               |
