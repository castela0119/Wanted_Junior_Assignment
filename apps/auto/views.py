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

        data = {}

        ko_name       = Company.objects.filter(korean_name__icontains = word).exists()
        en_name       = Company.objects.filter(english_name__icontains = word).exists()
        category_name = Company.objects.filter(name__icontains = word).exists()

        if ko_name:
                objs  = Company.objects.filter(korean_name__icontains = word)
                for obj in objs:
                    data.append({
                        'word' : obj.company_ko
                    })

        if en_name:
            objs  = Company.objects.filter(english_name__icontains = word)
            for obj in objs:
                data.append({
                    'word' : obj.company_en
                })

        if category_name:
            objs = Company.objects.filter(name__icontains = word)
            for obj in objs:
                data.append({
                    'word' : obj.company_jn
                })
        
        return Response(data)
