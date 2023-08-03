# Generated by Django 3.2.20 on 2023-08-03 09:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='goal_reached',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=17),
        ),
        migrations.AlterField(
            model_name='report',
            name='number_in_group',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9000)]),
        ),
        migrations.AlterField(
            model_name='report',
            name='number_on_route',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9000)]),
        ),
    ]