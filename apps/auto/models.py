from pyexpat import model
from django.db import models

# Create your models here.
class Company(models.Model):

    company_ko = models.CharField(max_length=30)
    company_en = models.CharField(max_length=30)
    company_ja = models.CharField(max_length=30)
    tag_ko = models.CharField(max_length=30)
    tag_en = models.CharField(max_length=30)
    tag_ja = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return  self.company_ko