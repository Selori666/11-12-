# utils.py — көмекші модуль

def add_film(films, name, rating):
    films[name] = rating
    print(f"'{name}' фильмі қосылды!")
    return films

def delete_film(films, name):
    if name in films:
        del films[name]
        print(f"'{name}' фильмі жойылды!")
    else:
        print("Ондай фильм табылмады.")
    return films

def find_film(films, name):
    if name in films:
        print(f"{name} рейтингі: {films[name]}")
    else:
        print("Ондай фильм жоқ.")