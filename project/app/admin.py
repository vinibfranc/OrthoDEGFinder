from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Organism, RealGene, AnnotedGene, FunctionalAnnotation

admin.site.site_header = 'Fungi Orthologs DE Platform'
admin.site.site_title = 'Fungi Orthologs DE Platform'

# Modelos que aparecem no admin e seus respectivos filtros

@admin.register(Organism)
class OrganismAdmin(admin.ModelAdmin):
    list_display = ('taxid', 'genus', 'species', 'lineage_strain')
    search_fields = ('taxid', 'genus', 'species', 'lineage_strain', 'genes__accession_number')
admin.register(RealGene)
@admin.register(RealGene)
class RealGeneAdmin(admin.ModelAdmin):
    list_display = ('accession_number', 'locus_tag')
    search_fields = ('accession_number','locus_tag')
@admin.register(AnnotedGene)
class AnnotedGeneAdmin(ImportExportModelAdmin):
    list_display = ('de_gene', 'log_fc', 'log_cpm', 'f', 'p_value', 'fdr')
    search_fields = ('de_gene', 'log_fc', 'p_value')
@admin.register(FunctionalAnnotation)
class FunctionalAnnotationAdmin(ImportExportModelAdmin):
    list_display = ('protein_id', 'go_id', 'ontology', 'description')
    search_fields = ('protein_id', 'go_id', 'ontology', 'description')
