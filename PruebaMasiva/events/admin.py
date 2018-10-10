from django.contrib import admin
from django.contrib.admin import AdminSite
from entities.models import *
from events.models import *

# Register your models here.
class EventAdminSite(AdminSite):
    site_header = "Events Admin"
    site_title = "Events Admin Portal"
    index_title = "Welcome to Researcher Events Portal"

event_admin_site = EventAdminSite(name='event_admin')

event_admin_site.register(Epic)
event_admin_site.register(Event)
event_admin_site.register(EventHero)
event_admin_site.register(EventVillain)
