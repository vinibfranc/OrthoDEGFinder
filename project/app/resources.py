from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget, FloatWidget, CharWidget, DecimalWidget, IntegerWidget, BooleanWidget
from .models import Organism, AnalysisAnnotatedGene, Pannzer2Annotation, Ortholog, ExperimentalDesign
import import_export.admin

class AnalysisAnnotatedGeneResource(resources.ModelResource):
    organism = fields.Field(column_name='organism', attribute='organism', widget=ForeignKeyWidget(Organism, 'taxid'))
    experimental_design = fields.Field(column_name='experimental_design', attribute='experimental_design', widget=ForeignKeyWidget(ExperimentalDesign, 'description'))
    de_gene = fields.Field(column_name='de_gene', attribute='de_gene', widget=CharWidget())
    log_fc = fields.Field(column_name='log_fc', attribute='log_fc', widget=FloatWidget())
    log_cpm = fields.Field(column_name='log_cpm', attribute='log_cpm', widget=FloatWidget())
    f = fields.Field(column_name='f', attribute='f', widget=FloatWidget())
    p_value = fields.Field(column_name='p_value', attribute='p_value', widget=FloatWidget())
    fdr = fields.Field(column_name='fdr', attribute='fdr', widget=FloatWidget())
    real_differential_expression = fields.Field(column_name='real_differential_expression', attribute='real_differential_expression', widget=BooleanWidget())
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    class Meta:
        model = AnalysisAnnotatedGene
        fields = ('organism', 'experimental_design', 'de_gene', 'log_fc', 'log_cpm', 'f', 'p_value', 'fdr', 'id')

class Pannzer2AnnotationResource(resources.ModelResource):
    organism = fields.Field(column_name='organism', attribute='organism', widget=ForeignKeyWidget(Organism, 'taxid'))
    protein_id = fields.Field(column_name='protein_id', attribute='protein_id', widget=CharWidget())
    go_id = fields.Field(column_name='go_id', attribute='go_id', widget=CharWidget())
    ontology = fields.Field(column_name='ontology', attribute='ontology', widget=CharWidget())
    description = fields.Field(column_name='ontology', attribute='ontology', widget=CharWidget())
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    class Meta:
        model = Pannzer2Annotation
        fields = ('organism', 'protein_id', 'go_id', 'ontology', 'description', 'id')