# Generated by Django 3.0.7 on 2020-06-09 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Adress',
            new_name='adress',
        ),
    ]
