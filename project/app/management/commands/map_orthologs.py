#encoding: utf-8

from django.core.management.base import BaseCommand
from app.models import Ortholog, Organism
import sys
import os
import re
import csv

class Command(BaseCommand):

    def csv_to_orthologs(self):
        orthologs = [] #'+sys.argv[1]+'.py'
        id_ortho = 0
        with open('app/orthologs/metarhizium_anisopliae__v__metarhizium_robertsii_format.tsv','r', encoding="utf-8", errors="ignore") as f:
            orthologs = csv.reader(f, delimiter='\t')
            for row in orthologs:
                #try:
                #org1_id = Organism.objects.get(taxid=int(row[0])).id
                #print(org1_id)
                #org2_id = Organism.objects.get(taxid=int(row[1])).id
                #print(org2_id)
                org_1_int = int(row[0])
                print(org_1_int)
                org_2_int = int(row[1])
                print(org_2_int)
                org_1 = Organism.objects.get(taxid__iexact=org_1_int).id
                org_2 = Organism.objects.get(taxid__iexact=org_2_int).id
                print(org_1)
                print(org_2)
                #print(id_ortho)

                print(row)

                #org_1_result = org_1.organism_1.add(org_1)
                #org_1 = Organism.objects.filter(taxid__iexact=row[0])[:1].get()
                ortholog = Ortholog.objects.create(pk=id_ortho,orthogroup=str(row[2]), organism_1=org_1, 
                            orthologs_organism_1=str(row[3]), organism_2=org_2, 
                            orthologs_organism_2=str(row[4]))
                ortholog.save()
                #except (ValueError):
                        #pass
                id_ortho += 1

    def handle(self, *args, **options):
        #self.map_orthologs()
        self.csv_to_orthologs()

def main():
    command = Command()

if __name__ == '__main__':
    main()