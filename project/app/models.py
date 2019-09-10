from django.db import models

class Organism(models.Model):
    taxid = models.IntegerField(verbose_name="Taxonomic ID", unique=True)
    kingdom = models.CharField(max_length=100)
    phylum = models.CharField(max_length=100)
    tax_class = models.CharField(max_length=100, verbose_name="Class")
    order = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    scientific_name_with_strain = models.CharField(max_length=300, verbose_name="Scientific name with strain")
    annotation_reference_organism = models.CharField(max_length=300, null=True)

    class Meta:
        ordering = ['taxid']
        verbose_name = 'Organism'
        verbose_name_plural = 'Organisms'

    def __str__(self):
        return self.scientific_name_with_strain

class ExperimentalDesign(models.Model):
    description = models.CharField(max_length=200, unique=True)
    condition_1 = models.CharField(max_length=20)
    condition_2 = models.CharField(max_length=20)
    replicate_number = models.IntegerField()
    organism = models.ForeignKey('Organism', on_delete=models.CASCADE, to_field='taxid', null=True)

    def __str__(self):
        return self.description

class GeneCorrespondences(models.Model):
    gene = models.ForeignKey('AnalysisAnnotatedGene', on_delete=models.CASCADE, null=True)
    annotation = models.ForeignKey('Pannzer2Annotation', on_delete=models.CASCADE, null=True)
    organism = models.ForeignKey('ExperimentalDesign', on_delete=models.CASCADE, null=True)
    ortholog = models.ForeignKey('Ortholog', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['gene']
        verbose_name = 'Gene correspondences'
        verbose_name_plural = 'Gene correspondences'

    def __str__(self):
        return str(self.gene)

class AnalysisAnnotatedGene(models.Model):
    organism = models.ForeignKey('Organism', on_delete=models.CASCADE, to_field='taxid', null=True)
    experimental_design = models.ForeignKey('ExperimentalDesign', on_delete=models.CASCADE, to_field='description', null=True)
    de_gene = models.CharField(max_length=10)
    log_fc = models.FloatField(null=True)
    log_cpm = models.FloatField(null=True)
    f = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)

    class Meta:
        ordering = ['log_fc', '-p_value', 'de_gene']
        verbose_name = 'Analysis Annotated gene'
        verbose_name_plural = 'Analysis Annotated genes'

    def __str__(self):
        return self.de_gene

class Pannzer2Annotation(models.Model):
    protein_id = models.CharField(max_length=20)
    go_id = models.IntegerField()
    ontology = models.CharField(max_length=5)
    description = models.CharField(max_length=200)
    organism = models.ForeignKey('Organism', on_delete=models.CASCADE, to_field='taxid', null=True)

    class Meta:
        ordering = ['description']
        verbose_name = 'Pannzer2 Functional annotation'
        verbose_name_plural = 'Pannzer2 Functional annotations'

    def __str__(self):
        return self.protein_id

class Ortholog(models.Model):
    orthogroup = models.CharField(max_length=20)
    organism_1 = models.ForeignKey('Organism', on_delete=models.CASCADE, related_name='organism_1', null=True)
    orthologs_organism_1 = models.CharField(max_length=500)
    organism_2 = models.ForeignKey('Organism', on_delete=models.CASCADE, related_name='organism_2', null=True)
    orthologs_organism_2 = models.CharField(max_length=500)

    class Meta:
        ordering = ['orthogroup']
        verbose_name = 'Orthologs'
        verbose_name_plural = 'Orthologs'
    
    def __str__(self):
        return self.orthogroup