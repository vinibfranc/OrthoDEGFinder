from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget, FloatWidget, CharWidget, DecimalWidget, IntegerWidget
from .models import Organism, AnalysisAnnotatedGene, Pannzer2Annotation, Ortholog, ExperimentalDesign
import import_export.admin

class AnalysisAnnotatedGeneResource(resources.ModelResource):
    organism = fields.Field(column_name='organism', attribute='organism', widget=ForeignKeyWidget(Organism, 'taxid'))
    design = fields.Field(column_name='experimental_design', attribute='experimentaldesign', widget=ForeignKeyWidget(ExperimentalDesign, 'description'))
    de_gene = fields.Field(column_name='de_gene', attribute='de_gene', widget=CharWidget())
    log_fc = fields.Field(column_name='log_fc', attribute='log_fc', widget=FloatWidget())
    log_cpm = fields.Field(column_name='log_cpm', attribute='log_cpm', widget=FloatWidget())
    f = fields.Field(column_name='f', attribute='f', widget=FloatWidget())
    p_value = fields.Field(column_name='p_value', attribute='p_value', widget=FloatWidget())
    fdr = fields.Field(column_name='fdr', attribute='fdr', widget=FloatWidget())
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    class Meta:
        model = AnalysisAnnotatedGene

class Pannzer2AnnotationResource(resources.ModelResource):
    organism = fields.Field(column_name='organism', attribute='organism', widget=ForeignKeyWidget(Organism, 'taxid'))
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    class Meta:
        model = Pannzer2Annotation

# class OrthologResource(resources.ModelResource):
#     organism_1 = fields.Field('Organism', column_name='organism_1', attribute='organism_1', widget=ForeignKeyWidget(Organism, 'lineage_strain'))
#     organism_2 = fields.Field('Organism', column_name='organism_2', attribute='organism_2', widget=ForeignKeyWidget(Organism, 'lineage_strain'))
#     skip_unchanged = True
#     report_skipped = True
#     exclude = ('id',)
#     class Meta:
#         model = Ortholog