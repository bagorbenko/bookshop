# Generated by Django 4.1.5 on 2023-01-15 23:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(
                decimal_places=2, default=0, editable=False, max_digits=10
            ),
        ),
    ]
