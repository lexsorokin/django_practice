# Generated by Django 3.2.15 on 2022-10-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market_place', '0004_alter_goods_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='sold',
            field=models.IntegerField(default=0, verbose_name='Продано шт.'),
        ),
    ]
