from django.db import models
from users.models import User

# Create your models here.
class Order(models.Model):
    title = models.CharField("Название", max_length = 100)
    adress = models.CharField('Адрес', max_length = 50)
    desc = models.TextField('Описание')
    is_arendated = models.BooleanField("Арендовано" ,default = False)
    date = models.DateField('Дата', auto_now = True)
    price = models.IntegerField('Цена за месяц аренды', null = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    img_outside = models.ImageField("Фото снаружи", upload_to = 'photo_outside/')
    img_inside = models.ImageField("Фото внутри", upload_to = 'photo_inside/')

    def __str__(self):
        return f'{self.author} {self.title} {self.price}'