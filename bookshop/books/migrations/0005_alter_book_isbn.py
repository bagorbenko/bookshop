# Generated by Django 4.1.5 on 2023-01-24 00:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_alter_bookinstance_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=models.CharField(max_length=13, unique=True, verbose_name="isbn"),
        ),
    ]
