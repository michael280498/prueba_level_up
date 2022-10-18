# Generated by Django 3.2.16 on 2022-10-18 02:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0002_formul2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formul2',
            name='id',
        ),
        migrations.AlterField(
            model_name='formul2',
            name='carne',
            field=models.TextField(primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 6', regex='^[A|a][a-zA-Z0-9][5][a-zA-Z0-9][a-zA-Z0-9][1|3|9]$')]),
        ),
    ]
