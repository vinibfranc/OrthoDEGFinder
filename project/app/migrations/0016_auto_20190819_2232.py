# Generated by Django 2.2.4 on 2019-08-20 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190819_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisannotatedgene',
            name='f',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='analysisannotatedgene',
            name='fdr',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='analysisannotatedgene',
            name='log_cpm',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='analysisannotatedgene',
            name='p_value',
            field=models.FloatField(null=True),
        ),
    ]