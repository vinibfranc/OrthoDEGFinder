# Generated by Django 2.2.4 on 2019-09-10 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190910_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genecorrespondences',
            name='organism',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ExperimentalDesign'),
        ),
    ]