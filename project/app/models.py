from django.db import models

class Organism(models.Model):
    taxid = models.IntegerField(verbose_name="Taxonomic ID", unique=True)
    kingdom = models.CharField(max_length=100)
    phylum = models.CharField(max_length=100)
    tax_class = models.CharField(max_length=100, verbose_name="Class")
    order = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    lineage_strain = models.CharField(max_length=100, verbose_name="Lineage/strain")
    annotation_reference_organism = models.CharField(max_length=300, null=True)
    #real_genes = models.ManyToManyField('RealGene', blank=True, related_name='real_genes')

    class Meta:
        ordering = ['taxid']
        verbose_name = 'Organism'
        verbose_name_plural = 'Organisms'

    def __str__(self):
        return self.genus+" "+self.species+" "+self.lineage_strain

class RealGene(models.Model):
    accession_number = models.CharField(max_length=20) 
    locus_tag = models.CharField(max_length=20)
    organism = models.ForeignKey('Organism', on_delete=models.CASCADE)
    #annotation = models.ForeignKey('Pannzer2Annotation', on_delete=models.CASCADE, null=True)
    #de_genes = models.FileField(verbose_name="Differentially expressed genes", upload_to="", null=True)

    class Meta:
        ordering = ['accession_number']
        verbose_name = 'Real gene'
        verbose_name_plural = 'Real genes'

    def __str__(self):
        return self.accession_number

class AnalysisAnnotatedGene(models.Model):
    de_gene = models.CharField(max_length=10)
    log_fc = models.FloatField(null=True)
    log_cpm = models.FloatField(null=True)
    f = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    #organism = models.ForeignKey('Organism', on_delete=models.CASCADE)
    #genes = models.OneToOneField('RealGene', on_delete=models.CASCADE, primary_key=True)

    class Meta:
        ordering = ['log_fc', 'de_gene']
        verbose_name = 'Analysis Annotated gene'
        verbose_name_plural = 'Analysis Annotated genes'

    def __str__(self):
        return self.de_gene

class Pannzer2Annotation(models.Model):
    protein_id = models.CharField(max_length=20)
    go_id = models.IntegerField()
    ontology = models.CharField(max_length=5)
    description = models.CharField(max_length=200)
    #organism = models.ForeignKey('Organism', on_delete=models.CASCADE)

    class Meta:
        ordering = ['description']
        verbose_name = 'Pannzer2 Functional annotation'
        verbose_name_plural = 'Pannzer2 Functional annotations'

    def __str__(self):
        return self.description

class ExperimentalDesign(models.Model):
    description = models.CharField(max_length=200)
    condition_1 = models.CharField(max_length=20)
    condition_2 = models.CharField(max_length=20)
    replicate_number = models.IntegerField()
    organism = models.ForeignKey('Organism', on_delete=models.CASCADE)

class Ortholog(models.Model):
    orthogroup = models.CharField(max_length=20)
    organism_1 = models.ForeignKey('Organism', on_delete=models.CASCADE, related_name='organism_1', null=True) #to_field='taxid'
    orthologs_organism_1 = models.CharField(max_length=500)
    organism_2 = models.ForeignKey('Organism', on_delete=models.CASCADE, related_name='organism_2', null=True) #to_field='taxid'
    orthologs_organism_2 = models.CharField(max_length=500)
    #annoted_genes = models.ManyToManyField('AnnotedGene', blank=True, related_name='real_genes')

    class Meta:
        ordering = ['orthogroup']
        verbose_name = 'Orthogroup'
        verbose_name_plural = 'Orthogroups'