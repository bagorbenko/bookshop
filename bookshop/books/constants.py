from django.db import models


class States(models.TextChoices):
    NEW = "N"
    USED = "U"
    BOOKSTATE = [
        (NEW, "новая"),
        (USED, "б.у."),
    ]


class Binding(models.TextChoices):
    SOFTCOVER = "SC"
    HARDCOVER = "HC"
    SPRING = "SP"
    BRACKET = "BR"
    BOLTED = "BL"
    BINDINGTYPE = [
        (SOFTCOVER, "мягкий"),
        (HARDCOVER, "твердый"),
        (SPRING, "металлическая пружина"),
        (BRACKET, "скоба"),
        (BOLTED, "на болтах"),
    ]
