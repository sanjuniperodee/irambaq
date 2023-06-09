# Generated by Django 2.2 on 2023-05-02 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20230331_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemimage',
            name='post',
        ),
        migrations.RemoveField(
            model_name='refund',
            name='order',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='being_delivered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='coupon',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='received',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ref_code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='refund_granted',
        ),
        migrations.RemoveField(
            model_name='order',
            name='refund_requested',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='v_obrabotke',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.DeleteModel(
            name='ItemImage',
        ),
        migrations.DeleteModel(
            name='Refund',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
