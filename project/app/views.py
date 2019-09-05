from django.shortcuts import render
from .models import Organism, ExperimentalDesign, AnalysisAnnotatedGene, Pannzer2Annotation, Ortholog, GeneCorrespondences
from .filters import OrganismDesignFilter, AnalysisAnnotatedGeneFilter, Pannzer2AnnotationFilter, OrthologFilter, UnifiedOrganismFilter, UnifiedGeneFilter, UnifiedAnnotationFilter                                                                                                                        
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request, 'home.html')

def search_organism(request):
    organism_list = ExperimentalDesign.objects.all()
    organism_filter = OrganismDesignFilter(request.GET, queryset=organism_list)
    return render(request, 'filters/organism_list.html', {'filter': organism_filter})

def search_gene(request):
    gene_list = AnalysisAnnotatedGene.objects.all()
    gene_filter = AnalysisAnnotatedGeneFilter(request.GET, queryset=gene_list)
    return render(request, 'filters/gene_list.html', {'filter': gene_filter})

def search_annotation(request):
    annotation_list = Pannzer2Annotation.objects.all()
    annotation_filter = Pannzer2AnnotationFilter(request.GET, queryset=annotation_list)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(annotation_filter, 10)
    # try:
    #     users = paginator.page(page)
    # except PageNotAnInteger:
    #     users = paginator.page(1)
    # except EmptyPage:
    #     users = paginator.page(paginator.num_pages)
    return render(request, 'filters/annotation_list.html', {'filter': annotation_filter})

def search_orthologs(request):
    orthologs_list = Ortholog.objects.all()
    orthologs_filter = OrthologFilter(request.GET, queryset=orthologs_list)
    return render(request, 'filters/orthologs_list.html', {'filter': orthologs_filter})

def search_unified_organism(request):
    return render(request, 'filters/unified_organism_list.html')

def search_unified_gene(request):
    return render(request, 'filters/unified_gene_list.html')

def search_unified_annotation(request):
    return render(request, 'filters/unified_annotatation_list.html')