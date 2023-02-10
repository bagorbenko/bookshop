# Generated by Django 4.1.5 on 2023-01-15 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                ("biography", models.TextField(blank=True, verbose_name="Описание")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="media/authors/",
                        verbose_name="Изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "isbn",
                    models.CharField(max_length=13, unique=True, verbose_name="ISBN"),
                ),
                (
                    "summary",
                    models.TextField(
                        blank=True, max_length=1000, verbose_name="Описание"
                    ),
                ),
                ("pages_count", models.PositiveIntegerField()),
                (
                    "state",
                    models.CharField(
                        choices=[("N", "Новая"), ("U", "Б.У.>")],
                        default="N",
                        max_length=2,
                    ),
                ),
                (
                    "bind",
                    models.CharField(
                        choices=[
                            ("SC", "Мягкая"),
                            ("HC", "Твердая"),
                            ("SP", "Пружинная"),
                            ("BR", "Скобой"),
                            ("BL", "Болтом"),
                        ],
                        default="SC",
                        max_length=2,
                    ),
                ),
                (
                    "author",
                    models.ManyToManyField(
                        related_name="books", to="books.author", verbose_name="автор"
                    ),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Категория")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
            },
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                ("description", models.TextField(verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Издательство",
                "verbose_name_plural": "Издательства",
            },
        ),
        migrations.CreateModel(
            name="BookInstances",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.FloatField(max_length=10, verbose_name="Цена")),
                ("count", models.PositiveIntegerField(verbose_name="Количество")),
                (
                    "book",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="price",
                        to="books.book",
                        verbose_name="Книга",
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="books.publisher",
                        verbose_name="Издательство",
                    ),
                ),
            ],
            options={
                "verbose_name": "Книга Издателя",
                "verbose_name_plural": "Книги Издателя",
            },
        ),
        migrations.AddField(
            model_name="book",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="books",
                to="books.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="genres",
            field=models.ManyToManyField(
                related_name="books", to="books.genre", verbose_name="жанры"
            ),
        ),
    ]
