import django_filters
from app.models import Organism, ExperimentalDesign, AnalysisAnnotatedGene, Pannzer2Annotation, Ortholog, GeneCorrespondences

CHOICES = (
    ('ascending', 'Ascending'),
    ('descending', 'Descending')
)

class OrganismDesignFilter(django_filters.FilterSet):
    organism__taxid = django_filters.CharFilter(lookup_expr='iexact', label='Tax ID')
    organism__kingdom = django_filters.CharFilter(lookup_expr='iexact', label='Kingdom')
    organism__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism')
    organism__annotation_reference_organism = django_filters.CharFilter(lookup_expr='icontains', label='Reference annotation')
    description = django_filters.CharFilter(lookup_expr='icontains', label='Experimental design')
    condition_1 = django_filters.CharFilter(lookup_expr='icontains', label='Condition 1')
    condition_2 = django_filters.CharFilter(lookup_expr='icontains', label='Condition 2')
    class Meta:
        model = ExperimentalDesign
        fields = ['organism__taxid', 'organism__kingdom', 'organism__scientific_name_with_strain', 'organism__annotation_reference_organism', 
                    'description', 'condition_1', 'condition_2']

class AnalysisAnnotatedGeneFilter(django_filters.FilterSet):
    experimental_design__description = django_filters.CharFilter(lookup_expr='icontains', label='Design')
    organism__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism')
    de_gene = django_filters.CharFilter(lookup_expr='icontains', label='DE Gene')
    log_fc = django_filters.NumberFilter(lookup_expr='startswith', label='Log FC')
    log_cpm = django_filters.NumberFilter(lookup_expr='startswith', label='Log CPM')
    f = django_filters.NumberFilter(lookup_expr='startswith', label='F')
    p_value = django_filters.NumberFilter(lookup_expr='startswith', label='P Value')
    fdr = django_filters.NumberFilter(lookup_expr='startswith', label='FDR')
    #log_fc_ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')
    class Meta:
        model = AnalysisAnnotatedGene
        fields = ['organism__scientific_name_with_strain', 'experimental_design__description','de_gene', 'log_fc', 'log_cpm', 'f', 'p_value', 'fdr']
    
    #def filter_by_order(self, queryset, name, value):
        #expression = 'log_fc' if value == 'ascending' else '-log_fc'
        #return queryset.order_by(expression)

class Pannzer2AnnotationFilter(django_filters.FilterSet):
    organism__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism')
    protein_id = django_filters.CharFilter(lookup_expr='icontains', label='Protein ID')
    go_id = django_filters.CharFilter(lookup_expr='icontains', label='GO ID')
    ontology = django_filters.CharFilter(lookup_expr='iexact', label='Ontology')
    description = django_filters.CharFilter(lookup_expr='icontains', label='Description')
    class Meta:
        model = Pannzer2Annotation
        fields = ['protein_id', 'go_id', 'ontology', 'description']

class OrthologFilter(django_filters.FilterSet):
    orthogroup = django_filters.CharFilter(lookup_expr='icontains', label='Orthogroup')
    organism_1__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism 1')
    orthologs_organism_1 = django_filters.CharFilter(lookup_expr='icontains', label='Ortholog organism 1')
    organism_2__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism 2')
    orthologs_organism_2 = django_filters.CharFilter(lookup_expr='icontains', label='Ortholog organism 2')
    class Meta:
        model = Ortholog
        fields = ['orthogroup', 'organism_1', 'orthologs_organism_1', 'organism_2', 'orthologs_organism_2']

class UnifiedFilter(django_filters.FilterSet):
    gene__de_gene = django_filters.CharFilter(lookup_expr='icontains', label='Gene')
    gene__log_fc = django_filters.CharFilter(lookup_expr='icontains', label='Log FC')
    gene__p_value = django_filters.CharFilter(lookup_expr='icontains', label='P Value')
    annotation__protein_id = django_filters.CharFilter(lookup_expr='icontains', label='Protein ID')
    annotation__go_id = django_filters.CharFilter(lookup_expr='icontains', label='GO ID')
    annotation__ontology = django_filters.CharFilter(lookup_expr='icontains', label='Ontology')
    annotation__description = django_filters.CharFilter(lookup_expr='icontains', label='Description')
    # TO-DO: relationship between Organism and Ortholog to filter
    class Meta:
        model = GeneCorrespondences
        fields = ['gene__de_gene', 'gene__log_fc', 'gene__p_value', 'annotation__protein_id', 'annotation__go_id', 'annotation__ontology', 'annotation__description']