from django.urls import path
from django.conf.urls import url

# from templates import ImagesListView
from . import templates;
from django.views.generic import (CreateView, DetailView, ListView)
from .templates import *
from . import views;

app_name = 'images'

urlpatterns = [

    path('', views.ImagesListView, name="list"),
    path('create', views.ImageCreate, name="create"),
    path('<pk>', views.DetailView, name="detail"),
    path('comment/create', views.DetailView, name="detail"),
    path('comment/delete/<image_pk>/<pk>', views.CommentDelete, name="comment_delete"),
    path('comment/edit/<comment_pk>/<pk>', views.CommentEdit, name="comment_edit"),

]
