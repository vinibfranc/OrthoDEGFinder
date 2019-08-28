#encoding: utf-8

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from app.models import AnalysisAnnotatedGene, Pannzer2Annotation, GeneCorrespondences
from Bio import Entrez, SeqIO
import sys
import os

class Command(BaseCommand):

    def map_genes_to_annotation(self):

        Entrez.email = "viniciusfr@ufcspa.edu.br"

        print("Mapping protein annotation and genes...")

        pannzer2_query = list(set(Pannzer2Annotation.objects.all().values_list("protein_id", flat=True)))
        #print(pannzer2_query)
        print("Annotations to be searched against NCBI Gene: {}".format(len(pannzer2_query)))

        de_genes_query = list(AnalysisAnnotatedGene.objects.all().values_list("de_gene", flat=True))
        #print(de_genes_query)

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
            #print(pannzer2)
            #print(locus_tag)

        #locus_tag_set = list(set(locus_tag))
        #print(len(locus_tag_set))
        #print(locus_tag_set)
        relation_dict = dict(zip(pannzer2, locus_tag))
        print(relation_dict)
        handle.close()

        id_corresp = 0
        for k, v in relation_dict.items():
            try:
                annot = Pannzer2Annotation.objects.filter(protein_id__iexact=str(k))[:1].get()
                gene_c = AnalysisAnnotatedGene.objects.get(de_gene__iexact=str(v))
                gene_create = GeneCorrespondences.objects.create(gene=gene_c, annotation=annot)
                gene_create.save()
                id_corresp += 1
                print(id_corresp)
            except (ValueError, AnalysisAnnotatedGene.DoesNotExist) as e:
                pass



        # for j in range(len(de_genes_query)):
        #     for k in range(len(locus_tag)):

    def handle(self, *args, **options):
        self.map_genes_to_annotation()

def main():
    command = Command()

if __name__ == '__main__':
    main()