# Generated by Django 4.1.3 on 2022-11-19 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='user',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
