from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    img_src = models.URLField(blank=True, null=True)
    years_of_age = models.CharField(max_length=9)
    bio = models.TextField()
    works = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'author'
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    img_src = models.URLField(blank=True, null=True)
    publication_date = models.DateField()
    short_desc = models.TextField()

    class Meta:
        db_table = 'book'
        ordering = ['title']

    def __str__(self):
        return self.title

class BookDetail(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='details')
    description = models.TextField()

    class Meta:
        db_table = 'book_detail'

    def __str__(self):
        return f'Details of {self.book.title}'