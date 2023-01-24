# Generated by Django 4.1.5 on 2023-01-24 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(max_length=13, unique=True, verbose_name='isbn'),
        ),
    ]
