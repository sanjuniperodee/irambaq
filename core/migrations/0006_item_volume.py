# Generated by Django 2.2 on 2022-09-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220807_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='volume',
            field=models.IntegerField(default=100),
        ),
    ]
