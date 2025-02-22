# Generated by Django 5.1.6 on 2025-02-22 10:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_partner_remove_employee_company_delete_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='company',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partner',
            name='participation',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MaxValueValidator(100.0)]),
        ),
    ]
