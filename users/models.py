from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    types = (
        ('s', 'Арендодатель'),
        ('b', "Арендатор")
    )
    account_type = models.CharField('Тип аккаунта', max_length = 1, choices = types)
    fio = models.CharField('ФИО', max_length = 150)
    phone = models.CharField('Телефон', max_length = 30)


