from import_export import resources
from .models import AnnotedGene, FunctionalAnnotation

class AnnotedGeneResource(resources.ModelResource):
    class Meta:
        model = AnnotedGene

class FunctionalAnnotationResource(resources.ModelResource):
    class Meta:
        model = FunctionalAnnotation