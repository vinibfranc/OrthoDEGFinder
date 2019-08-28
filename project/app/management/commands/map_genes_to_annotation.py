#encoding: utf-8

from django.core.management.base import BaseCommand
from app.models import AnalysisAnnotatedGene, Pannzer2Annotation, GeneCorrespondences
from Bio import Entrez, SeqIO
import sys
import os

class Command(BaseCommand):

    def map_genes_to_annotation(self):

        Entrez.email = "viniciusfr@ufcspa.edu.br"

        pannzer2_query = list(Pannzer2Annotation.objects.all().values_list("protein_id", flat=True))
        #print(pannzer2)

        de_genes_query = list(AnalysisAnnotatedGene.objects.all().values_list("de_gene", flat=True))
        #print(de_genes)

        locus_tag = []
        pannzer2 = []

        for i in range(len(pannzer2_query)):
            print(pannzer2_query[i])
            handle = Entrez.efetch(db="protein", id="{}".format(pannzer2_query[i]), idtype="acc", rettype="gb", retmode="text")
            record = SeqIO.read(handle, "genbank")
            #print(record)
            
            for feats in record.features:
                if feats.type == "CDS":
                    gene_list = feats.qualifiers["locus_tag"]
                    gene = gene_list[0]
                    #print(gene)
                    locus_tag.append(gene)
                    pannzer2.append(pannzer2_query[i])
                else:
                    pass
            print(pannzer2)
            print(len(pannzer2))
            print(locus_tag)
            print(len(pannzer2))
        relation_dict = dict(zip(pannzer2, locus_tag))
        print(relation_dict)
        handle.close()

        for k, v in relation_dict.items():
            print(v)

        # for j in range(len(de_genes_query)):
        #     for k in range(len(locus_tag)):

    def handle(self, *args, **options):
        self.map_genes_to_annotation()

def main():
    command = Command()

if __name__ == '__main__':
    main()