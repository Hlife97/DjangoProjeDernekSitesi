# Generated by Django 3.0.7 on 2020-06-06 01:33

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200605_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayarlar',
            name='phone2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='ayarlar',
            name='hakkimizda',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='ayarlar',
            name='iletisim',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='ayarlar',
            name='referanslar',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
