from django.db import models

class Organism(models.Model):
    taxid = models.IntegerField(verbose_name="Taxonomic ID")
    kingdom = models.CharField(max_length=100)
    phylum = models.CharField(max_length=100)
    tax_class = models.CharField(max_length=100, verbose_name="Class")
    order = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    lineage_strain = models.CharField(max_length=100, verbose_name="Lineage/strain")
    annotation_reference_organism = models.CharField(max_length=100, null=True)
    real_genes = models.ManyToManyField('RealGene', blank=True, related_name='real_genes')

    class Meta:
        ordering = ['taxid']
        verbose_name = 'Organism'
        verbose_name_plural = 'Organisms'

    def __str__(self):
        return self.genus+" "+self.species+" "+self.lineage_strain

class RealGene(models.Model):
    accession_number = models.CharField(max_length=20) 
    locus_tag = models.CharField(max_length=20)
    annotation = models.ForeignKey('FunctionalAnnotation', on_delete=models.CASCADE, null=True)
    de_genes = models.FileField(verbose_name="Differentially expressed genes", upload_to="", null=True)

    class Meta:
        ordering = ['accession_number']
        verbose_name = 'Real gene'
        verbose_name_plural = 'Real genes'

    def __str__(self):
        return self.accession_number

# TO-DO: upload file to populate it!
class AnnotedGene(models.Model):
    de_gene = models.CharField(max_length=10)
    log_fc = models.FloatField()#(match="logFC")
    log_cpm = models.FloatField()#(match="logCPM")
    f = models.FloatField()#(match="F")
    p_value = models.FloatField()#(match="PValue")
    fdr = models.FloatField()#(match="FDR")
    #genes = models.OneToOneField('RealGene', on_delete=models.CASCADE, primary_key=True)

    class Meta:
        ordering = ['de_gene']
        verbose_name = 'Annotated gene'
        verbose_name_plural = 'Annotated genes'

    def __str__(self):
        return self.de_gene

# TO-DO: upload file to populate it!
class FunctionalAnnotation(models.Model):
    protein_id = models.CharField(max_length=20)
    go_id = models.IntegerField()
    ontology = models.CharField(max_length=5)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ['description']
        verbose_name = 'Functional annotation'
        verbose_name_plural = 'Functional annotations'

    def __str__(self):
        return self.description

class Ortholog(models.Model):
    orthogroup = models.CharField(max_length=20)
    #annoted_genes = models.ManyToManyField('AnnotedGene', blank=True, related_name='real_genes')
