# Generated by Django 3.0.7 on 2020-06-05 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200605_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='Categori',
            new_name='categori',
        ),
    ]
