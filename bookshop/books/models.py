from django.db import models
from .constants import States, Binding


class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=150)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Author(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    biography = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to="media/authors/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Publisher(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"



class Book(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True,
                                 related_name="books")
    genres = models.ManyToManyField(Genre, verbose_name="жанры", related_name="books")
    author = models.ManyToManyField(Author, verbose_name="автор", related_name="books")
    isbn = models.CharField(verbose_name="ISBN", max_length=13, unique=True)
    summary = models.TextField(verbose_name="Описание", max_length=1000)
    pages_count = models.PositiveIntegerField()
    state = models.TextField(choices=States.choices, default=States.NEW, editable=True)
    bind = models.TextField(choices=Binding.choices, default=Binding.SOFTCOVER, editable=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class BookInstances(models.Model):
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE, null=True, related_name="price")
    publisher = models.ForeignKey(Publisher, verbose_name="Издательство", on_delete=models.SET_NULL, null=True)
    price = models.FloatField(verbose_name='Цена', max_length=10)
    count = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.book.title} - {self.publisher.name} - {self.price} - {self.count}'

    class Meta:
        verbose_name = "Книга Издателя"
        verbose_name_plural = "Книги Издателя"
