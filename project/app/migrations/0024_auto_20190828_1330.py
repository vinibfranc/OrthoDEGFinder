# Generated by Django 2.2.4 on 2019-08-28 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20190828_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genecorrespondences',
            options={'ordering': ['gene'], 'verbose_name': 'Gene correspondences', 'verbose_name_plural': 'Gene correspondences'},
        ),
        migrations.RemoveField(
            model_name='genecorrespondences',
            name='organism',
        ),
    ]