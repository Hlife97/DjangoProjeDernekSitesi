# Generated by Django 3.0.7 on 2020-06-07 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20200607_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='place',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
