#encoding: utf-8

import urllib3
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from app.models import Organism, ExperimentalDesign, AnalysisAnnotatedGene, Pannzer2Annotation, GeneCorrespondences, Ortholog
from Bio import Entrez, SeqIO
import sys
import os

# Change here the organisms taxids and the comrresponding design if you have others to compare
ORGANISM_1 = 1276135
ORGANISM_2 = 655844
EXP_DESIGN = "infect48hXinfect144h"

class Command(BaseCommand):

    def map_genes_to_annotation(self):

        Entrez.email = "viniciusfr@ufcspa.edu.br"
        Entrez.api_key = "e8515ac4bfc635f5afc2d74d8ad121863008"

        print("Mapping protein annotation and genes...")

        org1_query = list(Ortholog.objects.all().values_list("organism_1__taxid", flat=True))
        ortho1_query = list(Ortholog.objects.all().values_list("orthologs_organism_1__protein_id", flat=True))
        org2_query = list(Ortholog.objects.all().values_list("organism_2__taxid", flat=True))
        ortho2_query = list(Ortholog.objects.all().values_list("orthologs_organism_2__protein_id", flat=True))
        print(ortho1_query)
        print(ortho2_query)

        print("Annotations to be searched against NCBI Gene to Organism 1: {}".format(len(ortho1_query)))

        idx = 0
        try:
            for a, b, c, d in zip(org1_query, ortho1_query, org2_query, ortho2_query):
                print("{}: {} <-> {}".format(idx, b, d))
                handle_1 = Entrez.efetch(db="protein", id="{}".format(b), idtype="acc", rettype="gb", retmode="text")
                record_1 = SeqIO.read(handle_1, "genbank")
                handle_2 = Entrez.efetch(db="protein", id="{}".format(d), idtype="acc", rettype="gb", retmode="text")
                record_2 = SeqIO.read(handle_2, "genbank")
                idx += 1

                try:
                    for feats_1, feats_2 in zip(record_1.features, record_2.features):
                        if feats_1.type == "CDS" or feats_2.type == "CDS":
                            gene_list_1 = feats_1.qualifiers["locus_tag"]
                            gene_1 = gene_list_1[0]
                            print(gene_1)
                            gene_list_2 = feats_2.qualifiers["locus_tag"]
                            gene_2 = gene_list_2[0]
                            print(gene_2)
                            org_1 = Organism.objects.get(taxid__iexact=a)
                            org_2 = Organism.objects.get(taxid__iexact=c)
                            design = ExperimentalDesign.objects.get(description__iexact=EXP_DESIGN)
                            # annot_1 = Pannzer2Annotation.objects.filter(protein_id__iexact=b)[:1].get()
                            # annot_2 = Pannzer2Annotation.objects.filter(protein_id__iexact=d)[:1].get()
                            protein_organism_1 = Pannzer2Annotation.objects.filter(protein_id__iexact=b)[:1].get()
                            protein_organism_2 = Pannzer2Annotation.objects.filter(protein_id__iexact=d)[:1].get()
                            gene_organism_1 = AnalysisAnnotatedGene.objects.get(de_gene__iexact=gene_1)
                            print("---------> Gene", gene_organism_1)
                            print(gene_organism_1)
                            try:
                                gene_organism_2 = AnalysisAnnotatedGene.objects.get(de_gene__iexact=gene_2)
                            except AnalysisAnnotatedGene.DoesNotExist:
                                #pass
                                gene_organism_2 = AnalysisAnnotatedGene.objects.create(de_gene=gene_2)
                                gene_organism_2.save()
                            
                            corresp_object = GeneCorrespondences.objects.create(organism_1=org_1, organism_2=org_2, design=design, 
                                                                                gene_organism_1=gene_organism_1, gene_organism_2=gene_organism_2, 
                                                                                protein_organism_1=protein_organism_1, protein_organism_2=protein_organism_2)
                            corresp_object.save()
                except (KeyError, Pannzer2Annotation.DoesNotExist, AnalysisAnnotatedGene.DoesNotExist, Ortholog.DoesNotExist) as e:
                    pass 
        except urllib3.exceptions.HTTPError as e:
            pass
    
    def handle(self, *args, **options):
        self.map_genes_to_annotation()

def main():
    command = Command()

if __name__ == '__main__':
    main()