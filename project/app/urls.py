from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search_organism/', views.search_organism, name='search_organism'),
    path('search_gene/', views.search_gene, name='search_gene'),
    path('search_annotation/', views.search_annotation, name='search_annotation'),
    path('search_orthologs/', views.search_orthologs, name='search_orthologs'),
    path('search_unified_organism/', views.search_unified_organism, name='search_unified_organism'),
    path('search_unified_gene/', views.search_unified_gene, name='search_unified_gene'),
    path('search_unified_annotation/', views.search_unified_annotation, name='search_unified_annotation'),
]
