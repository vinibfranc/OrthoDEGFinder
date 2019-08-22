# Generated by Django 2.2.4 on 2019-08-22 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20190820_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organism',
            name='taxid',
            field=models.IntegerField(unique=True, verbose_name='Taxonomic ID'),
        ),
        migrations.AlterField(
            model_name='ortholog',
            name='organism_1',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organism_1', to='app.Organism', to_field='taxid'),
        ),
        migrations.AlterField(
            model_name='ortholog',
            name='organism_2',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organism_2', to='app.Organism', to_field='taxid'),
        ),
    ]
