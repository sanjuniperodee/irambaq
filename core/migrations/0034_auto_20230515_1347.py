# Generated by Django 2.2 on 2023-05-15 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_order_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]
