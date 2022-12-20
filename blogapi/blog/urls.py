from django.urls import path
from django.conf import urls
from .views import *

urlpatterns=[
    path("create", create_view,name="create"),
    
]