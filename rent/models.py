from django.db import models
from users.models import Seller

# Create your models here.
class Order(models.Model):
    title = models.CharField("Название", max_length = 100)
    desc = models.TextField('Описание')
    date = models.DateField('Дата', auto_now = True)
    price = models.IntegerField()
    author = models.OneToOneField(Seller, on_delete = models.CASCADE)
    img_outside = models.ImageField("Фото снаружи", upload_to = 'photo_outside/')
    img_inside = models.ImageField("Фото внутри", upload_to = 'photo_inside/')

    def __str__(self):
        return f'{self.author} {self.title}{self.price}'