from django.shortcuts import render
from apps.auto.models import Company
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AutoSearchAPI(APIView):
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        word = request.GET.get('word', '')

        data = []

        ko_name       = Company.objects.filter(company_ko__icontains = word).exists()
        en_name       = Company.objects.filter(company_en__icontains = word).exists()
        ja_name       = Company.objects.filter(company_ja__icontains = word).exists()

        if ko_name:
                objs  = Company.objects.filter(company_ko__icontains = word)
                for obj in objs:
                    data.append({
                        'word' : obj.company_ko
                    })

        if en_name:
            objs  = Company.objects.filter(company_en__icontains = word)
            for obj in objs:
                data.append({
                    'word' : obj.company_en
                })

        if ja_name:
            objs = Company.objects.filter(company_ja__icontains = word)
            for obj in objs:
                data.append({
                    'word' : obj.company_ja
                })
        
        return Response(data)
