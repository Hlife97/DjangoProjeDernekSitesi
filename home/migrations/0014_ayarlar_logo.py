# Generated by Django 3.0.7 on 2020-06-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200606_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayarlar',
            name='logo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
