from django.contrib import admin
from django.contrib.admin import AdminSite
from entities.models import *
from events.models import *
import csv
from django.http import HttpResponse
#from models import Post
from django import forms
from django.urls import path
from events.admin import event_admin_site
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count

# Register your models here.
class EntitiesAdminSite(AdminSite):
    site_header = "Entities Admin"
    site_title = "Entities Admin Portal"
    index_title = "Welcome to Researcher Entities Portal"

admin.site.register(Category)
#admin.site.register(Origin)
#admin.site.register(Hero)
#admin.site.register(Villain)

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ("name", "hero_count", "villain_count")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _hero_count=Count("hero", distinct=True),
            _villain_count=Count("villain", distinct=True),
        )
        return queryset

    def hero_count(self, obj):
        return obj._hero_count

    def villain_count(self, obj):
        return obj._villain_count
    hero_count.admin_order_field = '_hero_count'
    villain_count.admin_order_field = '_villain_count'


class IsVeryBenevolentFilter(admin.SimpleListFilter):
    title = 'is_very_benevolent'
    parameter_name = 'is_very_benevolent'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(benevolence_factor__gt=75)
        elif value == 'No':
            return queryset.exclude(benevolence_factor__gt=75)
        return queryset

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "category", "origin")
    actions = ["export_as_csv"]

    change_list_template = "entities/heroes_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            #path('entity-admin/', admin.site.urls),
            #path('event-admin/', event_admin_site.urls),
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.reader(csv_file)
            # Create Hero objects from passed in data
            
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "is_immortal", "category", "origin", "is_very_benevolent")
    actions = ["export_as_csv"]
    list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)

    def is_very_benevolent(self, obj):
        return obj.benevolence_factor > 75

    is_very_benevolent.boolean = True

    actions = ["mark_immortal"]
    def mark_immortal(self, request, queryset):
       queryset.update(is_immortal=True)

    change_list_template = "entities/heroes_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv)
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.reader(csv_file)
            # Create Hero objects from passed in data
            # ...
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )
