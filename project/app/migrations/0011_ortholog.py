# Generated by Django 2.2.4 on 2019-08-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190819_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ortholog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orthogroup', models.CharField(max_length=20)),
                ('orthologs_organism_1', models.CharField(max_length=500)),
                ('orthologs_organism_2', models.CharField(max_length=500)),
            ],
        ),
    ]