
from django.urls import path
from django.conf.urls import url

#from templates import ImagesListView
from . import templates;
from django.views.generic import (CreateView,DetailView,ListView)
from .templates import *
from . import views;

app_name='images'

urlpatterns = [

    path('',views.ImagesListView,name="list"),
    path('create',views.ImageCreate,name="create"),

]