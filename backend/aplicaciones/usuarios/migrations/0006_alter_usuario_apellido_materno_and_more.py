# Generated by Django 5.0.3 on 2024-03-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_usuario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido_materno',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido_paterno',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(),
        ),
    ]
