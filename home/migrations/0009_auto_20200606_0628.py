# Generated by Django 3.0.7 on 2020-06-06 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200606_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='status',
            field=models.CharField(blank=True, choices=[('True', 'Cevlandi'), ('False', 'Cevaplanmadi')], default='Cevaplanmadi', max_length=20),
        ),
    ]
