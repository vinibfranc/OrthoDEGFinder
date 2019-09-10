from django.shortcuts import render
from .models import Organism, ExperimentalDesign, AnalysisAnnotatedGene, Pannzer2Annotation, Ortholog, GeneCorrespondences
from .filters import OrganismDesignFilter, AnalysisAnnotatedGeneFilter, Pannzer2AnnotationFilter, OrthologFilter, UnifiedFilter                                                                                                                        
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import ListView

def home(request):
    return render(request, 'home.html')

def search_organism(request):
    organism_list = ExperimentalDesign.objects.all()
    organism_filter = OrganismDesignFilter(request.GET, queryset=organism_list)
    return render(request, 'filters/organism_list.html', {'filter': organism_filter})

def search_gene(request):
    ret = request.GET or None
    if(ret == None):
        gene_list = AnalysisAnnotatedGene.objects.none()
    else:
        gene_list = AnalysisAnnotatedGene.objects.all()
    gene_filter = AnalysisAnnotatedGeneFilter(request.GET, queryset=gene_list)
    return render(request, 'filters/gene_list.html', {'filter': gene_filter})

def search_annotation(request):
    ret = request.GET or None
    if(ret == None):
        annotation_list = Pannzer2Annotation.objects.none()
    else:
        annotation_list = Pannzer2Annotation.objects.all()
    annotation_filter = Pannzer2AnnotationFilter(request.GET, queryset=annotation_list)
    return render(request, 'filters/annotation_list.html', {'filter': annotation_filter})

def search_orthologs(request):
    ret = request.GET or None
    if(ret == None):
        orthologs_list = Ortholog.objects.none()
    else:
        orthologs_list = Ortholog.objects.all()
    orthologs_filter = OrthologFilter(request.GET, queryset=orthologs_list)
    return render(request, 'filters/orthologs_list.html', {'filter': orthologs_filter})
 
def search_unified(request):
    unified_list = GeneCorrespondences.objects.all()
    unified_filter = UnifiedFilter(request.GET, queryset=unified_list)
    return render(request, 'filters/unified_list.html', {'filter': unified_filter})