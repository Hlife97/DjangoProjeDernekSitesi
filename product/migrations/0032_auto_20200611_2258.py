# Generated by Django 3.0.7 on 2020-06-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0031_auto_20200611_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
