# Generated by Django 5.1.6 on 2025-02-25 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_company_alter_partner_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11)]),
        ),
    ]
