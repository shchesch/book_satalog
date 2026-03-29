import django
import os

# Устанавливаем переменную окружения для настроек Django-проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_catalog_settings')

# Инициализируем Django
django.setup()

# Импортируем модели
from books.models import Author, Book, BookDetail

# Удаляем все записи из таблиц, чтобы не было дублирования данных
Author.objects.all().delete()
Book.objects.all().delete()
BookDetail.objects.all().delete()

authors = [
    Author(id=1, name='Лев толстой', img_src='', years_of_age='1828-1910',
        bio='Русский писатель, философ, публицист, родоначальник толстовства.',
        works='Война и мир, Анна Каренина'),
    Author(id=2, name='Федор достоевский', img_src='', years_of_age='1821-1881',
        bio='Один из величайших русских писателей, мыслитель, философ.',
        works='Преступление и наказание, Идиот'),
    Author(id=3, name='Александр пушкин', img_src='', years_of_age='1799-1837',
        bio='Русский поэт, драматург, основоположник современного русского языка.',
        works='Евгений Онегин, Борис Годунов'),
    Author(id=4, name='Джордж оруэлл', img_src='', years_of_age='1903-1950',
        bio='Британский писатель и публицист, автор антиутопий.', works='1984, Скотный двор'),
    Author(id=5, name='Фрэнсис скотт фицджеральд', img_src='', years_of_age='1896-1948',
        bio='Американский писатель, мастер прозы.', works='Великий Гэтсби, Ночь нежна')]
Author.objects.create(authors)

books = [
    Book(id=1, title='война и мир', author_id=1, img_src=''),
    Book(id=2, title='преступление и наказание', author_id=2, img_src=''),
    Book(id=3, title='евриний онегин', author_id=3, img_src=''),
    Book(id=4, title='1984', author_id=4, img_src=''),
    Book(id=5, title='великий гэтсби', author_id=5, img_src=''),
]

# Массово добавляем информацию в базу данных
Book.objects.bulk_create(books)

book_details = [
    BookDetail(id=1, book_id=1, description='История семьи Ростовых, Болконских и других в эпоху наполеоновских войн.'),
    BookDetail(id=2, book_id=2, description='Психологический роман о студенте, который совершает убийство.'),
    BookDetail(id=3, book_id=3, description='Классический роман в стихах, рассказывающий о любви и трагедии.'),
    BookDetail(id=4, book_id=4, description='Иранный прогноз будущего, где Большой Брат следит за всеми.'),
    BookDetail(id=5, book_id=5, description='История любви и предательства в эпоху джаза.'),
]

# Массово добавляем информацию в базу данных
BookDetail.objects.create(book_details)

print('База данных успешно обновлена!')