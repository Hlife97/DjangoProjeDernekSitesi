# Generated by Django 3.0.7 on 2020-06-08 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20200607_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
