import os
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") 
django.setup()

from apps.auto.models import Company

CSV_PATH = './wanted_temp_data.csv'

def insert_company():

    with open(CSV_PATH, newline='') as csvfile:
        rows = csv.DictReader(csvfile)

        company_list = []
        
        for row in rows:
            company_list.append(Company(
                company_ko = row['company_ko'],
                company_en = row['company_en'],
                company_ja = row['company_ja'],
                tag_ko = row['tag_ko'],
                tag_en = row['tag_en'],
                tag_ja = row['tag_ja'],
            ))

        Company.objects.bulk_create(company_list)
        
        print('COMPANY DATA UPLOADED SUCCESSFULY!')
        

# insert_company()