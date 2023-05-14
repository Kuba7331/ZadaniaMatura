# Funkcja squarePower z argumentem x zwraca najwiekszy kwadrat znajdujacy sie w zakresie od 1 do x.

def squarePower(x):
    i = 1
    while True:
        if i * i > x:
            return (i-1) * (i-1)
        i += 1

# Przypisujemy wartosc sprawdzanej liczby.

number = int(input())
length = 0

# Petla wypisuje kwadraty liczb ktorych suma jest rowna zmiennej number. Jesli number jest wiekszy od 0, to do dlugosci reprezentacji kwadratowej liczby dodaje sie 1.

while number > 0:
        print(str(squarePower(number)))
        number = number - squarePower(number)
        length += 1

# Wypisanie dlugosci reprezentacji kwadratowej zmiennej number.

print("Dlugosc reprezentacji kwadratowej zmiennej number otrzymanej metoda zachlanna: ", str(length))
