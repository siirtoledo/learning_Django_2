from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("prime/",views.prime,name="prime"),
    path("prime/details/<str:id>",views.details, name="details"),
    
    
]