from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    types = (
        ('s', 'Продавец'),
        ('b', "Покупатель")
    )
    account_type = models.CharField(max_length = 1, choices = types)
    fio = models.CharField('ФИО', max_length = 150)
    phone = models.CharField('Телефон', max_length = 30)

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    ballance = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.user}'

