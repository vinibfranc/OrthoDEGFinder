#encoding: utf-8

from django.core.management.base import BaseCommand
from app.models import AnalysisAnnotatedGene, Pannzer2Annotation, Ortholog
from eutils import Client
from Bio import Entrez, SeqIO
import sys
import os
import re

class Command(BaseCommand):

    def map_genes_to_annotation(self):

        Entrez.email = "viniciusfr@ufcspa.edu.br"

        pannzer2 = list(Pannzer2Annotation.objects.all().values_list("protein_id", flat=True))
        print(pannzer2)

        de_genes = list(AnalysisAnnotatedGene.objects.all().values_list("de_gene", flat=True))
        print(de_genes)

        for i in range(len(pannzer2)):
            print(pannzer2[i])
            handle = Entrez.efetch(db="protein", id="{}".format(pannzer2[i]), idtype="acc", rettype="gb", retmode="text")
            record = SeqIO.read(handle, "genbank")
            #print(record)
            
            for f in record.features:
                #cds = [f for f in record.features if f.type == "CDS"]
                #print(cds)
                #print(cds.locus_tag)

                #print(f.qualifiers)
                #print(f.type)
                #if f.type == "CDS" and "gene" in f.qualifiers:
                #gene = f.qualifiers["gene"][0]
                # print(gene)
                # if gene in de_genes:
                #     print(f.qualifiers["gene"][0], f.qualifiers["locus_tag"][0])
        handle.close()

    def handle(self, *args, **options):
        self.map_genes_to_annotation()

def main():
    command = Command()

if __name__ == '__main__':
    main()