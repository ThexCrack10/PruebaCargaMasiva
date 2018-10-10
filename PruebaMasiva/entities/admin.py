from django.contrib import admin
from django.contrib.admin import AdminSite
from entities.models import *
from events.models import *

# Register your models here.
class EntitiesAdminSite(AdminSite):
    site_header = "Entities Admin"
    site_title = "Entities Admin Portal"
    index_title = "Welcome to Researcher Entities Portal"

admin.site.register(Category)
admin.site.register(Origin)
admin.site.register(Hero)
admin.site.register(Villain)

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)