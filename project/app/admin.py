from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Organism, RealGene, AnalysisAnnotatedGene, Pannzer2Annotation

admin.site.site_header = 'Fungi Orthologs DE Platform'
admin.site.site_title = 'Fungi Orthologs DE Platform'

# Modelos que aparecem no admin e seus respectivos filtros

class InLineRealGene(admin.StackedInline):
    model = RealGene
    extra = 0

class InLineAnalysisAnnotatedGene(admin.StackedInline):
    model = AnalysisAnnotatedGene
    extra = 0

class InLinePannzer2Annotation(admin.StackedInline):
    model = Pannzer2Annotation
    extra = 0

#@admin.register(Organism)
class OrganismAdmin(admin.ModelAdmin):
    list_display = ('taxid', 'genus', 'species', 'lineage_strain')
    search_fields = ('taxid', 'genus', 'species', 'lineage_strain', 'genes__accession_number')
    inlines = [InLineRealGene, InLineAnalysisAnnotatedGene, InLinePannzer2Annotation]
    fieldsets = (
        (None, {
            'fields': ('taxid', 'kingdom', 'phylum', 'tax_class', 'order', 'family', 'genus', 'species', 'lineage_strain', 'annotation_reference_organism')
        }),
    )
admin.site.register(Organism, OrganismAdmin)
# @admin.register(RealGene)
# class RealGeneAdmin(admin.ModelAdmin):
#     list_display = ('accession_number', 'locus_tag')
#     search_fields = ('accession_number','locus_tag')
# @admin.register(AnalysisAnnotatedGene)
# class AnalysisAnnotatedGeneAdmin(ImportExportModelAdmin):
#     list_display = ('de_gene', 'log_fc', 'log_cpm', 'f', 'p_value', 'fdr')
#     search_fields = ('de_gene', 'log_fc', 'p_value')
# @admin.register(Pannzer2Annotation)
# class Pannzer2AnnotationAdmin(ImportExportModelAdmin):
#     list_display = ('protein_id', 'go_id', 'ontology', 'description')
#     search_fields = ('protein_id', 'go_id', 'ontology', 'description')
