# Generated by Django 3.2.15 on 2022-10-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market_place', '0013_alter_goods_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='remaining_stock',
            field=models.PositiveIntegerField(null=True, verbose_name='Остаток'),
        ),
    ]
