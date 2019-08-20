# Generated by Django 2.2.4 on 2019-08-20 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190819_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='ortholog',
            name='organism_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organism_1', to='app.Organism'),
        ),
        migrations.AddField(
            model_name='ortholog',
            name='organism_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organism_2', to='app.Organism'),
        ),
    ]
