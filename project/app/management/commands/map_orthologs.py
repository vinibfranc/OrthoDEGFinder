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
        with open('app/orthologs/metarhizium_anisopliae__v__metarhizium_robertsii_format.tsv','r', encoding="utf-8", errors="ignore") as f:
            orthologs = csv.reader(f, delimiter='\t')
            for row in orthologs:
                org_1 = Organism.objects.get(taxid__iexact=row[0])
                org_2 = Organism.objects.get(taxid__iexact=row[1])
                #org_1 = Organism.objects.filter(taxid__iexact=row[0])[:1].get()
                #org_2 = Organism.objects.filter(taxid__iexact=row[1])[:1].get()
                #kwargs = {orthogroup=row[2], organism_1=3350, orthologs_organism_1=row[3], organism_2=655844, orthologs_organism_2=row[4]}
                ortholog = Ortholog(orthogroup=str(row[2]), organism_1=org_1, 
                            orthologs_organism_1=str(row[3]), organism_2=org_2, 
                            orthologs_organism_2=str(row[4]))
                #ortholog = Ortholog(**kwargs)
                # ortholog.save()
                # orthogroup = Ortholog.objects.get(orthogroup__iexact=row[0])
                # org_1 = Ortholog.objects.get(organism__iexact=row[1])
                # orthologs_org_1 = Ortholog.objects.get(organism__iexact=row[2])
                # org_2 = Ortholog.objects.get(organism__iexact=row[3])
                # orthologs_org_2 = Ortholog.objects.get(organism__iexact=row[4])
                print(row)
                # if ',' in row[3]:
                #     print(row[3])
                    # [[x] for x in row[3].split(',')]
                    #print("Done")
                    #print(row)
                    #for ortho_1 in row[3].split(','):
                        #orthologs.append([ortho_1])
                #print("Saiu")
                #print(orthologs)
                    # for ortho_1 in orthologs[row][3].split(','):
                    #     orthologs.append([ortho_1])  
                #print(row[3])
                #print(row[4])

    def handle(self, *args, **options):
        #self.map_orthologs()
        self.csv_to_orthologs()

def main():
    command = Command()

if __name__ == '__main__':
    main()