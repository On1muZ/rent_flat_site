# Generated by Django 4.1.3 on 2022-11-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0019_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Коментарий'),
        ),
    ]
