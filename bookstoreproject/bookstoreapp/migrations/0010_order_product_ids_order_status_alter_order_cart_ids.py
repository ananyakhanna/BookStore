# Generated by Django 4.0.6 on 2022-12-28 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreapp', '0009_order_contact_number_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_ids',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart_ids',
            field=models.CharField(max_length=200),
        ),
    ]
