from django.urls import path, include
from apps.auto.views import AutoSearchAPI

urlpatterns = [
    path('search', AutoSearchAPI.as_view())
]