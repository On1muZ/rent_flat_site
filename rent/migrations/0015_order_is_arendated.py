# Generated by Django 4.1.3 on 2022-11-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0014_alter_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_arendated',
            field=models.BooleanField(default=False),
        ),
    ]