# Generated by Django 3.2.15 on 2022-10-26 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_market_place', '0005_goods_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='sold',
        ),
    ]