# Generated by Django 3.2.15 on 2022-10-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market_place', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='remaining_stock',
            field=models.IntegerField(null=True, verbose_name='Остаток'),
        ),
    ]