def suma(list, counter, i):
    """  Funkcja która liczy sumę 2 liczb """
    if i == 1 or i == len(list) + 1:
        return 1
    else:
        suma = sum([list[i - 2], list[i - 1]])
        return suma


def dlugosc_ostatniej_linijki(n):
    """  brzydka funkcja która liczy ilość znaków ze spacjami w ostatniej linijce  """
    counter = 0
    list = []
    for i in range(0, n + 1):
        counter += 1
        x = []
        for i in range(1, counter + 1):
            if counter < 3:
                x.append(1)
            else:
                number = suma(list[len(list) - 1], counter, i)
                x.append(number)
        list.append(x)
    p = n
    for i in list[n]:
        x = len(str(i))
        p += x
    return p


def trojkąt(n):
    """  Funkcja która rysuje trójkąt  """
    counter = 0
    list = []
    for i in range(0, n + 1):

        spacje = " " * (n - counter)
        print(f"{counter}  ", end="")
        counter += 1
        x = []
        for i in range(1, counter + 1):
            if counter < 3:
                x.append(1)
            else:
                number = suma(list[len(list) - 1], counter, i)
                x.append(number)
        list.append(x)
        centrum = dlugosc_ostatniej_linijki(n)
        print(" ".join([str(i) for i in x]).center(centrum))
    drop = ". " * (n * 2)
    print(drop.center(centrum))
    print(centrum)


trojkąt(23)  # przykładowe wywołanie
