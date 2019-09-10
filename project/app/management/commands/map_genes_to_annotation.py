#encoding: utf-8

import urllib3
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from app.models import ExperimentalDesign, AnalysisAnnotatedGene, Pannzer2Annotation, GeneCorrespondences, Ortholog
from Bio import Entrez, SeqIO
import sys
import os

class Command(BaseCommand):

    def map_genes_to_annotation(self):

        Entrez.email = "viniciusfr@ufcspa.edu.br"
        Entrez.api_key = "e8515ac4bfc635f5afc2d74d8ad121863008"

        print("Mapping protein annotation and genes...")

        pannzer2_query = set(Pannzer2Annotation.objects.all().values_list("protein_id", "organism__taxid"))
        print(pannzer2_query)
        pannzer2_dict = dict(pannzer2_query)
        print(pannzer2_dict)
        print("Annotations to be searched against NCBI Gene: {}".format(len(pannzer2_query)))

        de_genes_query = AnalysisAnnotatedGene.objects.all().values_list("de_gene", "organism__taxid")
        print(de_genes_query)
        de_genes_dict = dict(de_genes_query)
        print(de_genes_dict)

        idx = 0
        try:
            for key, value in pannzer2_dict.items():
                print("{}: {} -> {}".format(idx, key, value))
                handle = Entrez.efetch(db="protein", id="{}".format(key), idtype="acc", rettype="gb", retmode="text")
                record = SeqIO.read(handle, "genbank")
                idx += 1

                try:
                    for feats in record.features:
                        if feats.type == "CDS":
                            gene_list = feats.qualifiers["locus_tag"]
                            gene = gene_list[0]
                            print(gene)
                            gene_c = AnalysisAnnotatedGene.objects.get(de_gene__iexact=gene)
                            annot = Pannzer2Annotation.objects.filter(protein_id__iexact=str(key))[:1].get()
                            # if(Ortholog.objects.filter(orthologs_organism_1__iexact=str(key))[:1].get() == Pannzer2Annotation.objects.filter(protein_id__iexact=str(key))[:1].get()):
                            #     ortho = Ortholog.objects.filter(orthologs_organism_2__iexact=str(key))[:1].get()
                            # elif(Ortholog.objects.filter(orthologs_organism_2__iexact=str(key))[:1].get() == Pannzer2Annotation.objects.filter(protein_id__iexact=str(key))[:1].get()):
                            #     ortho = Ortholog.objects.filter(orthologs_organism_1__iexact=str(key))[:1].get()
                            # else:
                            #     print("Entrou aqui!")
                            #     pass
                            organism_c = ExperimentalDesign.objects.get(organism__taxid__iexact=int(value))
                            gene_create = GeneCorrespondences.objects.create(gene=gene_c, annotation=annot, organism=organism_c)#, ortholog=ortho)
                            gene_create.save()
                except (AnalysisAnnotatedGene.DoesNotExist) as e:
                    pass 
        except urllib3.exceptions.HTTPError as e:
            pass
    
    def handle(self, *args, **options):
        self.map_genes_to_annotation()

def main():
    command = Command()

if __name__ == '__main__':
    main()