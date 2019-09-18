import django_filters
from app.models import Organism, ExperimentalDesign, AnalysisAnnotatedGene, Pannzer2Annotation, Ortholog, GeneCorrespondences

LOG_FC = (
    ('ascending', 'Ascending'),
    ('descending', 'Descending')
)

P_VALUE = (
    ('ascending', 'Ascending'),
    ('descending', 'Descending')
)

ONTOLOGY = (
    ('BP', 'BP'),
    ('CC', 'CC'),
    ('MF', 'MF')
)

class OrganismDesignFilter(django_filters.FilterSet):
    organism__taxid = django_filters.CharFilter(lookup_expr='iexact', label='Tax ID')
    organism__kingdom = django_filters.CharFilter(lookup_expr='iexact', label='Kingdom')
    organism__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism')
    organism__annotation_reference_organism = django_filters.CharFilter(lookup_expr='icontains', label='Reference annotation')
    description = django_filters.CharFilter(lookup_expr='icontains', label='Exp. design')
    condition_1 = django_filters.CharFilter(lookup_expr='icontains', label='Condition 1')
    condition_2 = django_filters.CharFilter(lookup_expr='icontains', label='Condition 2')
    class Meta:
        model = ExperimentalDesign
        fields = ['organism__taxid', 'organism__kingdom', 'organism__scientific_name_with_strain', 'organism__annotation_reference_organism', 
                    'description', 'condition_1', 'condition_2']

class AnalysisAnnotatedGeneFilter(django_filters.FilterSet):
    experimental_design__description = django_filters.CharFilter(lookup_expr='icontains', label='Exp. Design')
    organism__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism')
    de_gene = django_filters.CharFilter(lookup_expr='icontains', label='DE Gene')
    log_fc = django_filters.ChoiceFilter(label='Log2 FC', choices=LOG_FC, method='filter_log_fc')
    log_cpm = django_filters.NumberFilter(lookup_expr='startswith', label='Log CPM')
    f = django_filters.NumberFilter(lookup_expr='startswith', label='F')
    p_value = django_filters.ChoiceFilter(label='P Value', choices=P_VALUE, method='filter_p_value')
    fdr = django_filters.NumberFilter(lookup_expr='startswith', label='FDR')
    class Meta:
        model = AnalysisAnnotatedGene
        fields = ['organism__scientific_name_with_strain', 'experimental_design__description','de_gene', 'log_fc', 'log_cpm', 'f', 'p_value', 'fdr']
    
    def filter_log_fc(self, queryset, name, value):
        expression = 'log_fc' if value == 'ascending' else '-log_fc'
        return queryset.order_by(expression)
    
    def filter_p_value(self, queryset, name, value):
        expression = 'p_value' if value == 'ascending' else '-p_value'
        return queryset.order_by(expression)
    
class Pannzer2AnnotationFilter(django_filters.FilterSet):
    organism__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism')
    protein_id = django_filters.CharFilter(lookup_expr='icontains', label='Protein ID')
    go_id = django_filters.CharFilter(lookup_expr='icontains', label='GO ID')
    ontology = django_filters.ChoiceFilter(label='Ontology', choices=ONTOLOGY)
    description = django_filters.CharFilter(lookup_expr='icontains', label='Description')
    class Meta:
        model = Pannzer2Annotation
        fields = ['protein_id', 'go_id', 'ontology', 'description']

class OrthologFilter(django_filters.FilterSet):
    orthogroup = django_filters.CharFilter(lookup_expr='icontains', label='Orthogroup')
    organism_1__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism 1')
    orthologs_organism_1__protein_id = django_filters.CharFilter(lookup_expr='icontains', label='Ortholog organism 1')
    organism_2__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism 2')
    orthologs_organism_2__protein_id = django_filters.CharFilter(lookup_expr='icontains', label='Ortholog organism 2')
    class Meta:
        model = Ortholog
        fields = ['orthogroup', 'organism_1', 'orthologs_organism_1__protein_id', 'organism_2', 'orthologs_organism_2__protein_id']

class UnifiedFilter(django_filters.FilterSet):
    organism_1__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism 1')
    organism_2__scientific_name_with_strain = django_filters.CharFilter(lookup_expr='icontains', label='Organism 2')
    design__description = django_filters.CharFilter(lookup_expr='icontains', label='Design description')
    gene_organism_1__de_gene = django_filters.CharFilter(lookup_expr='icontains', label='Gene 1')
    gene_organism_2__de_gene = django_filters.CharFilter(lookup_expr='icontains', label='Gene 2')
    gene_organism_1__log_fc  = django_filters.ChoiceFilter(label='Log2 FC', choices=LOG_FC, method='filter_log_fc_unified')
    gene_organism_1__p_value = django_filters.ChoiceFilter(label='P Value', choices=P_VALUE, method='filter_p_value_unified')
    protein_organism_1__protein_id = django_filters.CharFilter(lookup_expr='icontains', label='Protein 1')
    protein_organism_2__protein_id = django_filters.CharFilter(lookup_expr='icontains', label='Protein 2')
    protein_organism_1__go_id = django_filters.CharFilter(lookup_expr='icontains', label='GO ID')
    protein_organism_1__ontology = django_filters.ChoiceFilter(label='Ontology', choices=ONTOLOGY)
    protein_organism_1__description = django_filters.CharFilter(lookup_expr='icontains', label='Description')
    
    def filter_log_fc_unified(self, queryset, name, value):
        expression = 'gene_organism_1__log_fc' if value == 'ascending' else '-gene_organism_1__log_fc'
        return queryset.order_by(expression)
    
    def filter_p_value_unified(self, queryset, name, value):
        expression = 'gene_organism_1__p_value' if value == 'ascending' else '-gene_organism_1__p_value'
        return queryset.order_by(expression)

    class Meta:
        model = GeneCorrespondences
        fields = ['organism_1__scientific_name_with_strain', 'organism_2__scientific_name_with_strain', 
                    'design__description', 'gene_organism_1__de_gene', 'gene_organism_2__de_gene', 
                    'gene_organism_1__log_fc', 'gene_organism_1__p_value', 'protein_organism_1__protein_id', 
                    'protein_organism_2__protein_id', 'protein_organism_1__go_id', 'protein_organism_1__ontology', 
                    'protein_organism_1__description']