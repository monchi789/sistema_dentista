# Generated by Django 5.0.3 on 2024-03-19 15:39

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_usuario_id_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
