from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Organism, AnalysisAnnotatedGene, Pannzer2Annotation, ExperimentalDesign, Ortholog, GeneCorrespondences
from .resources import AnalysisAnnotatedGeneResource, Pannzer2AnnotationResource

admin.site.site_header = 'Fungi Orthologs DE Platform'
admin.site.site_title = 'Fungi Orthologs DE Platform'

class InLineExperimentalDesign(admin.StackedInline):
    model = ExperimentalDesign
    extra = 0

class OrganismAdmin(admin.ModelAdmin):
    list_display = ('taxid', 'scientific_name_with_strain', 'annotation_reference_organism')
    search_fields = ('taxid', 'scientific_name_with_strain', 'annotation_reference_organism')
    inlines = [InLineExperimentalDesign]
    fieldsets = (
        (None, {
            'fields': ('taxid', 'kingdom', 'phylum', 'tax_class', 'order', 'family', 'scientific_name_with_strain', 'annotation_reference_organism')
        }),
    )
admin.site.register(Organism, OrganismAdmin)

@admin.register(GeneCorrespondences)
class GeneCorrespondencesAdmin(admin.ModelAdmin):
    # TO-DO
    pass
    # list_display = ('de_genes', 'protein_ids', 'functional_annotation_count')

    # def de_genes(self, obj):
    #     qs = AnalysisAnnotatedGene.objects.filter(de_gene=obj.gene).values('de_gene').order_by('de_gene')
    #     qs_str = ', '.join([str(qs[i]['de_gene']) for i,c in enumerate(qs)])
    #     return qs_str
        
    # def protein_ids(self, obj):
    #     qs = Pannzer2Annotation.objects.filter(protein_id=obj.annotation).first()
    #     return qs

    # def functional_annotation_count(self, obj):
    #     qs = Pannzer2Annotation.objects.filter(protein_id=obj.annotation).count()
    #     return qs

@admin.register(AnalysisAnnotatedGene)
class AnalysisAnnotatedGeneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('de_gene', 'log_fc', 'log_cpm', 'f', 'p_value', 'fdr', 'organism', 'experimental_design')
    search_fields = ('de_gene', 'log_fc', 'p_value')
    resource_class = AnalysisAnnotatedGeneResource

@admin.register(Pannzer2Annotation)
class Pannzer2AnnotationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('protein_id', 'go_id', 'ontology', 'description', 'organism')
    search_fields = ('protein_id', 'go_id', 'ontology', 'description')
    resource_class = Pannzer2AnnotationResource

@admin.register(Ortholog)
class OrthologAdmin(admin.ModelAdmin):
    list_display = ('orthogroup', 'organism_1', 'orthologs_organism_1', 'organism_2', 'orthologs_organism_2')
    search_fields = ('orthogroup', 'orthologs_organism_1', 'orthologs_organism_2')