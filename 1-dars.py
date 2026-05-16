import time

class Book:
    def __init__(self, title, status="O'qilmoqda"):
        self.title = title
        self.status = status
        self.reading_time = 0

    def add_time(self, minutes):
        self.reading_time += minutes
        print(f"✅ '{self.title}' kitobiga {minutes} daqiqa qo'shildi.")

# Kutubxona ro'yxati
my_library = []

def add_book():
    name = input("Kitob nomini kiriting: ")
    new_book = Book(name)
    my_library.append(new_book)
    print(f"📖 '{name}' kutubxonangizga qo'shildi!")

def show_books():
    print("\n--- Mening Kutubxonam ---")
    for book in my_library:
        print(f"📚 {book.title} | Holati: {book.status} | Sarflangan vaqt: {book.reading_time} min")

# Dasturni ishga tushirish (kichik demo)
add_book()
show_books()