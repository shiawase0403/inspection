# Generated by Django 5.0.6 on 2024-08-05 15:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dorminspect',
            name='blbzj',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='blct',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='ccjh',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='ckjh',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='ctjh',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='ctzw',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='mc',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='mjh',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='room',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='scbzj',
            field=models.BooleanField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='scjh',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='scsz',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='wsmf',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='dorminspect',
            name='zlmf',
            field=models.BooleanField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
