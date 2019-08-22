# Generated by Django 2.2.4 on 2019-08-16 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_auto_20190816_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionalAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein_id', models.CharField(max_length=20)),
                ('go_id', models.IntegerField()),
                ('ontology', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Functional annotation',
                'verbose_name_plural': 'Functional annotations',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='RealGene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accession_number', models.CharField(max_length=20)),
                ('locus_tag', models.CharField(max_length=20)),
                ('annotation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.FunctionalAnnotation')),
            ],
            options={
                'verbose_name': 'Real gene',
                'verbose_name_plural': 'Real genes',
                'ordering': ['accession_number'],
            },
        ),
        migrations.CreateModel(
            name='AnnotedGene',
            fields=[
                ('de_gene', models.CharField(max_length=10)),
                ('log_fc', models.FloatField()),
                ('log_cpm', models.FloatField()),
                ('f', models.FloatField()),
                ('p_value', models.FloatField()),
                ('fdr', models.FloatField()),
                ('genes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.RealGene')),
            ],
            options={
                'verbose_name': 'Annotated gene',
                'verbose_name_plural': 'Annotated genes',
                'ordering': ['de_gene'],
            },
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxid', models.IntegerField(verbose_name='Taxonomic ID')),
                ('kingdom', models.CharField(max_length=100)),
                ('phylum', models.CharField(max_length=100)),
                ('tax_class', models.CharField(max_length=100, verbose_name='Class')),
                ('order', models.CharField(max_length=100)),
                ('family', models.CharField(max_length=100)),
                ('genus', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('lineage_strain', models.CharField(max_length=100, verbose_name='Lineage/strain')),
                ('annotation_reference_organism', models.CharField(max_length=100, null=True)),
                ('real_genes', models.ManyToManyField(blank=True, related_name='real_genes', to='app.RealGene')),
            ],
            options={
                'verbose_name': 'Organism',
                'verbose_name_plural': 'Organisms',
                'ordering': ['taxid'],
            },
        ),
    ]