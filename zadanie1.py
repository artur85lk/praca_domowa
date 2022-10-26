def suma(kolekcja):
    results = 0
    if type(kolekcja) is dict:
        for v in kolekcja.values():
            if type(v) is int:
                results += v
    else:
        for i in kolekcja:
            if type(i) is int:
                results += i
    return results










