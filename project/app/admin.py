from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Organism, AnalysisAnnotatedGene, Pannzer2Annotation, ExperimentalDesign, Ortholog, RealGene
from .resources import AnalysisAnnotatedGeneResource, Pannzer2AnnotationResource

admin.site.site_header = 'Fungi Orthologs DE Platform'
admin.site.site_title = 'Fungi Orthologs DE Platform'

class InLineRealGene(admin.StackedInline):
    model = RealGene
    extra = 0

class InLineExperimentalDesign(admin.StackedInline):
    model = ExperimentalDesign
    extra = 0

class OrganismAdmin(admin.ModelAdmin):
    list_display = ('taxid', 'genus', 'species', 'lineage_strain')
    search_fields = ('taxid', 'genus', 'species', 'lineage_strain', 'genes__accession_number')
    inlines = [InLineRealGene, InLineExperimentalDesign]
    fieldsets = (
        (None, {
            'fields': ('taxid', 'kingdom', 'phylum', 'tax_class', 'order', 'family', 'genus', 'species', 'lineage_strain', 'annotation_reference_organism')
        }),
    )
admin.site.register(Organism, OrganismAdmin)

@admin.register(AnalysisAnnotatedGene)
class AnalysisAnnotatedGeneAdmin(ImportExportModelAdmin):
    list_display = ('de_gene', 'log_fc', 'log_cpm', 'f', 'p_value', 'fdr')
    search_fields = ('de_gene', 'log_fc', 'p_value')
    resource_class = AnalysisAnnotatedGeneResource
@admin.register(Pannzer2Annotation)
class Pannzer2AnnotationAdmin(ImportExportModelAdmin):
    list_display = ('protein_id', 'go_id', 'ontology', 'description')
    search_fields = ('protein_id', 'go_id', 'ontology', 'description')
    resource_class = Pannzer2AnnotationResource
@admin.register(Ortholog)
class OrthologAdmin(admin.ModelAdmin):
    list_display = ('orthogroup', 'orthologs_organism_1', 'orthologs_organism_2')
    search_fields = ('orthogroup', 'orthologs_organism_1', 'orthologs_organism_2')
    #resource_class = OrthologResource

