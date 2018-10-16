from django.contrib import admin
from backend.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.admin import AdminSite
#CARGA MASIVA
from django import forms
from django.urls import path
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count

# Register your models here.

admin.site.register(RubroComercio)
admin.site.register(Categoria)
admin.site.register(Caracteristica)
admin.site.register(UnidadDeMedida)
admin.site.register(TipoCodigo)
admin.site.register(CaracteristicaProducto)
admin.site.register(CodigoProducto)
admin.site.register(MedidaProducto)
admin.site.register(Comercio)
#admin.site.register(Producto)

#-------------------------------------

@admin.register(Producto)
class ProductAdmin(ImportExportModelAdmin):
    pass 
    