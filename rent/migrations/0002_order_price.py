# Generated by Django 4.1.3 on 2022-11-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
