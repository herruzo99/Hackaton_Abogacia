# Generated by Django 2.2.1 on 2019-05-11 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='comentario',
            new_name='texto',
        ),
        migrations.AddField(
            model_name='articulo',
            name='tipo',
            field=models.IntegerField(default=0),
        ),
    ]
