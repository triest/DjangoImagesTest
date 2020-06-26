
from django.urls import path
from django.conf.urls import url

from Images.views import ImagesListView
from . import views;
from django.views.generic import (CreateView,DetailView,ListView)
from .views import *

app_name='images'

urlpatterns = [

    #path('', views.article_list,name="list"),
    path('',ImagesListView),

]