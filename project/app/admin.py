from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Organism, AnalysisAnnotatedGene, Pannzer2Annotation, ExperimentalDesign, Ortholog, GeneCorrespondences
from .resources import AnalysisAnnotatedGeneResource, Pannzer2AnnotationResource

admin.site.site_header = 'Ortho DEG Finder'
admin.site.site_title = 'Ortho DEG Finder'

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
    list_display = ('organism_1', 'organism_2', 'design', 'gene_organism_1', 'gene_organism_2', 
                    'protein_organism_1', 'protein_organism_2', 'functional_annotation_count')
    search_fields = ('organism_1__scientific_name_with_strain', 'organism_2__scientific_name_with_strain',
                    'design__description', 'gene_organism_1__de_gene', 'gene_organism_2__de_gene',
                    'protein_organism_1__protein_id', 'protein_organism_2__protein_id')

    def functional_annotation_count(self, obj):
        qs = Pannzer2Annotation.objects.filter(protein_id=obj.protein_organism_1).count()
        return qs

@admin.register(AnalysisAnnotatedGene)
class AnalysisAnnotatedGeneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('de_gene', 'log_fc', 'log_cpm', 'f', 'p_value', 'fdr', 'organism', 'experimental_design', 'real_differential_expression')
    search_fields = ('de_gene', 'log_fc', 'p_value', 'experimental_design__description', 'real_differential_expression')
    resource_class = AnalysisAnnotatedGeneResource

@admin.register(Pannzer2Annotation)
class Pannzer2AnnotationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('protein_id', 'go_id', 'ontology', 'description', 'organism')
    search_fields = ('protein_id', 'go_id', 'ontology', 'description', 'organism__scientific_name_with_strain')
    resource_class = Pannzer2AnnotationResource

@admin.register(Ortholog)
class OrthologAdmin(admin.ModelAdmin):
    list_display = ('orthogroup', 'organism_1', 'orthologs_organism_1', 'organism_2', 'orthologs_organism_2')
    search_fields = ('orthogroup', 'orthologs_organism_1', 'orthologs_organism_2')