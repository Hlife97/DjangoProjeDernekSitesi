# Generated by Django 3.0.7 on 2020-06-11 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_urun_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urun',
            name='Categori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Categori'),
        ),
    ]
