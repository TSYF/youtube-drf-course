# Generated by Django 4.2.2 on 2023-07-26 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_id_del_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='ID del Usuario',
            new_name='user',
        ),
    ]
