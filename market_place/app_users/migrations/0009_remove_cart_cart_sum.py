# Generated by Django 3.2.15 on 2022-10-23 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0008_auto_20221023_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_sum',
        ),
    ]
