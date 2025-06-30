from book import Book

# Создаем список книг (библиотеку)
library = [Book("Отверженнные", "Гюго"),
           Book("Князь", "Мазин"),
           Book("Мастер и Маргарита", "Булгаков")]
# Печатаем библиотеку
for book in library:
    print(f"{book.title} - {book.author}")
