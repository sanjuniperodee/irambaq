# Generated by Django 2.2 on 2023-05-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20230502_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='acrtiul',
        ),
        migrations.AddField(
            model_name='item',
            name='height',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
