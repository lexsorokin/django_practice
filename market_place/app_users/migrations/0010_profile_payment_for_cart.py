# Generated by Django 3.2.15 on 2022-10-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0009_remove_cart_cart_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='payment_for_cart',
            field=models.PositiveIntegerField(null=True, verbose_name='На оплату'),
        ),
    ]
