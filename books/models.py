from django.db import models


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Author(models.Model):
    name = models.CharField("Имя", max_length=100)
    biography = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="authors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Publisher(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class States(models.TextChoices):
    new = 'новая'
    used = 'б.у.'


class Binding(models.TextChoices):
    softcover = 'мягкий'
    hardcover = 'твердый'
    spring = 'металлическая пружина'
    bracket = 'скобой'
    bolted = 'на болтах'


class Book(models.Model):
    title = models.CharField("Название", max_length=100)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    author = models.ManyToManyField(Author, verbose_name="автор")
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    summary = models.TextField("Описание", max_length=1000)
    pages_count = models.PositiveIntegerField()
    state = models.TextField(choices=States.choices, default=States.new, editable=True)
    bind = models.TextField(choices=Binding.choices, default=Binding.softcover, editable=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class BookInstance(models.Model):
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.SET_NULL, null=True, related_name="price")
    publisher = models.ForeignKey(Publisher, verbose_name="Издательство", on_delete=models.SET_NULL, null=True)
    price = models.FloatField('Цена', max_length=10)
    count = models.PositiveIntegerField('Количество', )

    def __str__(self):
        return f'{self.book.title} - {self.publisher.name} - {self.price} - {self.count}'

    class Meta:
        verbose_name = "Книга Издателя"
        verbose_name_plural = "Книги Издателя"
