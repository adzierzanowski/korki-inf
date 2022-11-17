# SQL

- [SQL](#sql)
  - [SELECT FROM](#select-from)
    - [TOP](#top)
  - [WHERE](#where)
    - [Porównywanie napisów](#porównywanie-napisów)
  - [ORDER BY](#order-by)
    - [Sortowanie wg wielu kolumn](#sortowanie-wg-wielu-kolumn)
    - [DESC, ASC](#desc-asc)
  - [GROUP BY](#group-by)
    - [HAVING](#having)
  - [JOIN](#join)
    - [INNER JOIN](#inner-join)
    - [LEFT JOIN](#left-join)

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

### TOP

Jeżeli chcemy ograniczyć wynik do `n` pierwszych wierszy, to używamy `SELECT TOP`

```sql
-- Wybieramy 3 najstarsze osoby z tabeli
SELECT TOP 3 imie, nazwisko, wiek FROM osoby ORDER BY wiek DESC;
```

| imie                | nazwisko            | wiek                |
|---------------------|---------------------|---------------------|
| Janina              | Jankowska           | 66                  |
| Rafał               | Wiśniewski          | 46                  |
| Karol               | Krawczyk            | 38                  |

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

| id                  | imie                | nazwisko            | plec                | wiek                | miasto              |
|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| 3                   | Andrzej             | Pieczony            | M                   | 12                  | Tarnów              |
| 1                   | Jan                 | Kowalski            | M                   | 20                  | Warszawa            |
| 2                   | Anna                | Nowak               | K                   | 32                  | Kraków              |
| 6                   | Karol               | Krawczyk            | M                   | 38                  | Warszawa            |
| 7                   | Tadeusz             | Norek               | M                   | 38                  | Warszawa            |
| 8                   | Renata              | Wrzosek             | K                   | 38                  | Opole               |
| 4                   | Rafał               | Wiśniewski          | M                   | 46                  | Opole               |
| 5                   | Janina              | Jankowska           | K                   | 66                  | Warszawa            |



### Sortowanie wg wielu kolumn

Wiersze najpierw zostaną posortowane wg płci, a potem w obrębie danej płci - wg wieku:

```sql
SELECT * FROM osoby ORDER BY plec, wiek;
```

| id                  | imie                | nazwisko            | plec                | wiek                | miasto              |
|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| 2                   | Anna                | Nowak               | K                   | 32                  | Kraków              |
| 8                   | Renata              | Wrzosek             | K                   | 38                  | Opole               |
| 5                   | Janina              | Jankowska           | K                   | 66                  | Warszawa            |
| 3                   | Andrzej             | Pieczony            | M                   | 12                  | Tarnów              |
| 1                   | Jan                 | Kowalski            | M                   | 20                  | Warszawa            |
| 6                   | Karol               | Krawczyk            | M                   | 38                  | Warszawa            |
| 7                   | Tadeusz             | Norek               | M                   | 38                  | Warszawa            |
| 4                   | Rafał               | Wiśniewski          | M                   | 46                  | Opole               |

### DESC, ASC

Do każdej kolumny w `ORDER BY` możemy dołączyć modyfikator `DESC` lub `ASC`,

`DESC` sortuje kolumny nierosnąco, `ASC` - niemalejąco.

## GROUP BY

`GROUP BY` scala ze sobą wiersze, które mają identyczną wartość w danej kolumnie.

```sql
SELECT * FROM osoby GROUP BY miasto;
```

| id                  | imie                | nazwisko            | plec                | wiek                | miasto              |
|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| 2                   | Anna                | Nowak               | K                   | 32                  | Kraków              |
| 4                   | Rafał               | Wiśniewski          | M                   | 46                  | Opole               |
| 3                   | Andrzej             | Pieczony            | M                   | 12                  | Tarnów              |
| 1                   | Jan                 | Kowalski            | M                   | 20                  | Warszawa            |

Takie grupowanie nie miałoby żadnego sensu (bo w zgrupowanym wierszu widać tylko
informacje o jednej osobie), gdyby nie **funkcje agregujące**.
Tzn. takie funkcje, które dają nam informacje na temat scalonych wierszy.

```sql
SELECT miasto, Count(*) AS liczba_mieszkancow FROM osoby GROUP BY miasto;
```

| miasto              | liczba_mieszkancow  |
|---------------------|---------------------|
| Kraków              | 1                   |
| Opole               | 2                   |
| Tarnów              | 1                   |
| Warszawa            | 4                   |

### HAVING

Jeżeli chcemy ograniczyć wynik do wierszy spełniających pewien warunek
i odnosimy się do kolumn wykorzystujących funkcje agregujące, to zamiast
`WHERE` piszemy `HAVING`.

```sql
SELECT miasto, Count(*) AS liczba_mieszkancow
FROM osoby
GROUP BY miasto
HAVING Count(*) > 1;
```

| miasto              | liczba_mieszkancow  |
|---------------------|---------------------|
| Opole               | 2                   |
| Warszawa            | 4                   |

## JOIN

Tabele można łączyć wg kolumn. Przykładowo mamy tabelę zwierząt:

```sql
SELECT * FROM zwierzeta;
```

| id                  | id_osoby            | imie                | wiek                | gatunek             |
|---------------------|---------------------|---------------------|---------------------|---------------------|
| 1                   | 1                   | Azor                | 4                   | pies                |
| 2                   | 1                   | Fiflak              | 3                   | kot                 |
| 3                   | 4                   | Fortuna             | 2                   | papuga              |

Jeżeli chcemy wyświetlić osoby i ich zwierzęta, to możemy połączyć te tabele
wg kolumny `id_osoby`.

### INNER JOIN

`INNER JOIN` połączy te tabele i wyświetli wiersze tylko jeżeli w drugiej tabeli (zwierzeta)
znajdą się odpowiadające wiersze.

```sql
SELECT
  osoby.imie,
  osoby.nazwisko,
  zwierzeta.imie AS imie_zwierzecia,
  zwierzeta.wiek AS wiek_zwierzecia,
  zwierzeta.gatunek
FROM osoby
INNER JOIN zwierzeta
  ON osoby.id=zwierzeta.id_osoby;
```

| imie                | nazwisko            | imie_zwierzecia     | wiek_zwierzecia     | gatunek             |
|---------------------|---------------------|---------------------|---------------------|---------------------|
| Jan                 | Kowalski            | Azor                | 4                   | pies                |
| Jan                 | Kowalski            | Fiflak              | 3                   | kot                 |
| Rafał               | Wiśniewski          | Fortuna             | 2                   | papuga              |

### LEFT JOIN

Z kolei `LEFT JOIN` wybierze **wszystkie** wiersze z lewej tabeli (`osoby`)
niezależnie od tego, czy w prawej tabeli (`zwierzeta`) znajdą się wiersze
odpowiadające wybranej relacji (`osoby.id=zwierzeta.id_osoby`).


```sql
SELECT
  osoby.imie,
  osoby.nazwisko,
  zwierzeta.imie AS imie_zwierzecia,
  zwierzeta.wiek AS wiek_zwierzecia,
  zwierzeta.gatunek
FROM osoby
LEFT JOIN zwierzeta
  ON osoby.id=zwierzeta.id_osoby;
```

| imie                | nazwisko            | imie_zwierzecia     | wiek_zwierzecia     | gatunek             |
|---------------------|---------------------|---------------------|---------------------|---------------------|
| Jan                 | Kowalski            | Azor                | 4                   | pies                |
| Jan                 | Kowalski            | Fiflak              | 3                   | kot                 |
| Anna                | Nowak               | `NULL`                | `NULL`                | `NULL`                |
| Andrzej             | Pieczony            | `NULL`                | `NULL`                | `NULL`                |
| Rafał               | Wiśniewski          | Fortuna             | 2                   | papuga              |
| Janina              | Jankowska           | `NULL`                | `NULL`                | `NULL`                |
| Karol               | Krawczyk            | `NULL`                | `NULL`                | `NULL`                |
| Tadeusz             | Norek               | `NULL`                | `NULL`                | `NULL`                |
| Renata              | Wrzosek             | `NULL`                | `NULL`                | `NULL`                |

Możemy dzięki temu wybrać np. osoby, które nie mają zwierząt.

```sql
SELECT osoby.imie, osoby.nazwisko
FROM osoby
LEFT JOIN zwierzeta
  ON osoby.id=zwierzeta.id_osoby
WHERE zwierzeta.imie IS NULL;
```

| imie                | nazwisko            |
|---------------------|---------------------|
| Anna                | Nowak               |
| Andrzej             | Pieczony            |
| Janina              | Jankowska           |
| Karol               | Krawczyk            |
| Tadeusz             | Norek               |
| Renata              | Wrzosek             |
