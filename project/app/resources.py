from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from .models import Organism, AnalysisAnnotatedGene, Pannzer2Annotation, Ortholog
import import_export.admin

class AnalysisAnnotatedGeneResource(resources.ModelResource):
    organism = fields.Field(column_name='organism', attribute='organism', widget=ForeignKeyWidget(Organism, 'taxid'))
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

class OrthologResource(resources.ModelResource):
    organism_1 = fields.Field('Organism', column_name='organism_1', widget=ForeignKeyWidget(Organism, 'taxid'))
    organism_2 = fields.Field('Organism', column_name='organism_2', widget=ForeignKeyWidget(Organism, 'taxid'))
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    class Meta:
        model = Ortholog