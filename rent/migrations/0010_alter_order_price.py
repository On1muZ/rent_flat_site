# Generated by Django 4.1.3 on 2022-11-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0009_alter_order_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
