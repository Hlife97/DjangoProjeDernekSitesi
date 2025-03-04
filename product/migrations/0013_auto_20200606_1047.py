# Generated by Django 3.0.7 on 2020-06-06 07:47

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_categori_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categori',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categori',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categori',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categori',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categori',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.Categori'),
        ),
    ]
