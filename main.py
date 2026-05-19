import json
from pathlib import Path


BOOKS_FILE = Path("books.json")


def load_books():
    if not BOOKS_FILE.exists():
        return []

    with BOOKS_FILE.open("r", encoding="utf-8") as file:
        try:
            books = json.load(file)
        except json.JSONDecodeError:
            return []

    return books if isinstance(books, list) else []


def save_books(books):
    with BOOKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def input_required(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Поле не должно быть пустым.")


def input_rating():
    while True:
        value = input("Оценка (1-5): ").strip()

        if value.isdigit():
            rating = int(value)
            if 1 <= rating <= 5:
                return rating

        print("Ошибка: оценка должна быть целым числом от 1 до 5.")


def is_duplicate_book(books, author, title):
    for book in books:
        same_author = book["author"].lower() == author.lower()
        same_title = book["title"].lower() == title.lower()
        if same_author and same_title:
            return True
    return False


def add_book(books):
    author = input_required("Автор: ")
    title = input_required("Название: ")

    if is_duplicate_book(books, author, title):
        print("Такая книга уже есть в списке.")
        return

    rating = input_rating()
    read_date = input_required("Дата прочтения: ")

    books.append(
        {
            "author": author,
            "title": title,
            "rating": rating,
            "read_date": read_date,
        }
    )
    save_books(books)
    print("Книга добавлена.")


def show_books(books):
    if not books:
        print("Список книг пуст.")
        return

    for index, book in enumerate(books, start=1):
        print(
            f"{index}. {book['author']} - {book['title']}, "
            f"оценка: {book['rating']}, дата: {book['read_date']}"
        )


def show_average_rating(books):
    if not books:
        print("Нет книг для расчёта средней оценки.")
        return

    total = sum(book["rating"] for book in books)
    average = total / len(books)
    print(f"Средняя оценка: {average:.2f}")


def show_author_stats(books):
    if not books:
        print("Нет данных для статистики.")
        return

    stats = {}
    for book in books:
        author = book["author"]
        stats[author] = stats.get(author, 0) + 1

    for author, count in stats.items():
        print(f"{author}: {count}")


def delete_book(books):
    print("Удаление книги будет добавлено в отдельной ветке.")


def show_menu():
    print()
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")


def main():
    books = load_books()

    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            show_books(books)
        elif choice == "3":
            show_average_rating(books)
        elif choice == "4":
            show_author_stats(books)
        elif choice == "5":
            delete_book(books)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: выберите пункт от 1 до 6.")


if __name__ == "__main__":
    main()
