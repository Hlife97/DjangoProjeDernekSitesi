# Generated by Django 3.0.7 on 2020-06-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_auto_20200611_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urun',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
