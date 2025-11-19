from utilis import add_film, delete_film, find_film

# 11 апта: OOP (класс, атрибут, әдіс, мұрагерлік)

class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def info(self):
        return f"Фильм: {self.name}, рейтинг: {self.rating}"

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"{self.name} фильміне жаңа рейтинг қойылды: {self.rating}")


class AnimatedMovie(Movie):  # Movie класынан мұрагер
    def __init__(self, name, rating, studio):
        super().__init__(name, rating)
        self.studio = studio

    def info(self):
        return f"Анимация: {self.name}, рейтинг: {self.rating}, студия: {self.studio}"


def oop_demo():
    print("\n--- OOP МЫСАЛДАРЫ ---")

    film = Movie("Интерстеллар", 8.6)
    print(film.info())

    cartoon = AnimatedMovie("Тачки", 7.9, "Pixar")
    print(cartoon.info())

    cartoon.update_rating(8.2)
    print(cartoon.info())


# 12 апта: NumPy және Matplotlib
import numpy as np
import matplotlib.pyplot as plt


def ratings_to_numpy(films):
    ratings = np.array(list(films.values()))
    print("\n--- NumPy массиві ---")
    print("Массив:", ratings)
    print("Орташа рейтинг:", np.mean(ratings))
    return ratings


def plot_ratings(films):
    print("\n--- График салу ---")

    names = list(films.keys())
    ratings = list(films.values())

    plt.plot(names, ratings, marker="o")
    plt.title("Фильм рейтингтері динамикасы")
    plt.xlabel("Фильмдер")
    plt.ylabel("Рейтинг")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()



# 8 апта: функциялар мен логика

def show_films(films):
    print("\nФильмдер тізімі:")
    for name, rating in films.items():
        print(f"{name}: {rating}")


def ask_repeat():  # Рекурсия
    again = input("Қайтадан таңдауды қалайсыз ба? (иә/жоқ): ").lower()
    if again == "иә":
        menu()
    elif again == "жоқ":
        print("Бағдарлама аяқталды.")
    else:
        print("Қате енгізу. Қайта енгізіңіз.")
        ask_repeat()



# Бастапқы деректер

films = {
    "Выживший": 7.8,
    "Остров проклятых": 8.6,
    "Поймай меня, если сможешь": 8.5
}


# 10 апта: файлға сақтау/оқу

def save_to_file(films, filename="data.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for name, rating in films.items():
            f.write(f"{name}:{rating}\n")
    print("Мәліметтер файлға сақталды!")


def load_from_file(filename="data.txt"):
    films = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")
                if len(parts) == 2:
                    name, rating = parts
                    films[name] = float(rating)
                else:
                    print(f"⚠️ Қате форматтағы жол өткізіліп кетті: {line}")
    except FileNotFoundError:
        print("Файл табылмады, жаңа база жасалды.")
    return films



# 9 апта: try-except. Негізгі меню

def menu():
    global films
    while True:
        print("\nМәзір:")
        print("1 - Фильмдер тізімі")
        print("2 - Фильм қосу")
        print("3 - Фильм жою")
        print("4 - Рейтинг көру")
        print("5 - Файлға сақтау")
        print("6 - Файлдан оқу")
        print("7 - Шығу")
        print("8 - OOP демонстрациясы (Movie, AnimatedMovie)")
        print("9 - NumPy және график (Matplotlib)")

        choice = input("Таңдауыңыз: ")

        try:
            if choice == "1":
                show_films(films)
            elif choice == "2":
                name = input("Фильм атауы: ")
                rating = float(input("Рейтингі: "))
                films = add_film(films, name, rating)
            elif choice == "3":
                name = input("Жою үшін фильм атауы: ")
                films = delete_film(films, name)
            elif choice == "4":
                name = input("Фильм атауы: ")
                find_film(films, name)
            elif choice == "5":
                save_to_file(films)
            elif choice == "6":
                films = load_from_file()
                print("Файлдан деректер оқылды!")
            elif choice == "7":
                print("Бағдарлама аяқталды.")
                break
            elif choice == "8":
                oop_demo()
            elif choice == "9":
                arr = ratings_to_numpy(films)
                plot_ratings(films)
            else:
                print("Қате таңдау!")
        except ValueError:
            print("Рейтинг санмен енгізілуі керек!")
        except Exception as e:
            print("Қате:", e)

    ask_repeat()



# Бағдарламаны іске қосу


if __name__ == "__main__":
    films = load_from_file()
    menu()
