from django.conf.urls import url
from map.views import *

urlpatterns = [    
    url(r'^$', MapView.as_view(), name="index"),
    # url(r'^(?P<slug>[\w\-]+)$', MapDetailView.as_view(), name="detail"),
]