# Generated by Django 5.0.3 on 2024-03-19 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_alter_usuario_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
    ]