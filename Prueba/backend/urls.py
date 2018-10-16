from django.conf.urls import url
from backend.views import *

urlpatters = [
    url(r'^backend/$', ProductoList.as_view(), name="product")
]
