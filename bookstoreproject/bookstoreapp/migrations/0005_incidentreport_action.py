# Generated by Django 4.0.6 on 2022-12-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreapp', '0004_incidentreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentreport',
            name='action',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
