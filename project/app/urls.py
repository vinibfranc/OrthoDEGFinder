from django.contrib import admin
from django.urls import path
from app import views
# from app.views import OrganismListFilter

urlpatterns = [
    path('', views.home, name='home'),
    #path('search_organism/', OrganismListFilter.as_view(), name='search_organism'),
    path('search_organism/', views.search_organism, name='search_organism'),
    path('search_gene/', views.search_gene, name='search_gene'),
    path('search_annotation/', views.search_annotation, name='search_annotation'),
    path('search_orthologs/', views.search_orthologs, name='search_orthologs'),
    path('search_unified/', views.search_unified, name='search_unified'),
]
