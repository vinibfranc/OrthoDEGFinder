# Generated by Django 2.2.4 on 2019-09-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_analysisannotatedgene_real_differential_expression'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisannotatedgene',
            name='real_differential_expression',
            field=models.BooleanField(),
        ),
    ]
