# Generated by Django 3.1.5 on 2021-02-23 20:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210218_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['-creado'], 'verbose_name': 'categoria'},
        ),
        migrations.AlterField(
            model_name='entrada',
            name='categorias',
            field=models.ManyToManyField(related_name='get_entradas', to='blog.Categoria'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
