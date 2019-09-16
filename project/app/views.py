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
    paginator = Paginator(organism_filter.qs, 25)
    page = request.GET.get('page')
    page_organism = paginator.get_page(page)
    return render(request, 'filters/organism_list.html', {'filter': organism_filter, 'page_organism': page_organism})

def search_gene(request):
    gene_list = AnalysisAnnotatedGene.objects.all()
    gene_filter = AnalysisAnnotatedGeneFilter(request.GET, queryset=gene_list)
    paginator = Paginator(gene_filter.qs, 25)
    page = request.GET.get('page')
    page_gene = paginator.get_page(page)
    return render(request, 'filters/gene_list.html', {'filter': gene_filter, 'page_gene': page_gene})

def search_annotation(request):
    annotation_list = Pannzer2Annotation.objects.all()
    annotation_filter = Pannzer2AnnotationFilter(request.GET, queryset=annotation_list)
    paginator = Paginator(annotation_filter.qs, 25)
    page = request.GET.get('page')
    page_annotation = paginator.get_page(page)
    return render(request, 'filters/annotation_list.html', {'filter': annotation_filter, 'page_annotation': page_annotation})

def search_orthologs(request):
    orthologs_list = Ortholog.objects.all()
    orthologs_filter = OrthologFilter(request.GET, queryset=orthologs_list)
    paginator = Paginator(orthologs_filter.qs, 25)
    page = request.GET.get('page')
    page_orthologs = paginator.get_page(page)
    return render(request, 'filters/orthologs_list.html', {'filter': orthologs_filter, 'page_orthologs': page_orthologs})
 
def search_unified(request):
    unified_list = GeneCorrespondences.objects.all()
    unified_filter = UnifiedFilter(request.GET, queryset=unified_list)
    paginator = Paginator(unified_filter.qs, 25)
    page = request.GET.get('page')
    page_unified = paginator.get_page(page)
    return render(request, 'filters/unified_list.html', {'filter': unified_filter, 'page_unified': page_unified})