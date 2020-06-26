from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


#from .models import Image
from django.contrib.auth.decorators import login_required

#from . import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
# get_template is what we need for loading up the template for parsing.
from django.template.loader import get_template
from django.template import loader
# Templates in Django need a "Context" to parse with, so we'll borrow this.
# "Context"'s are really nothing more than a generic dict wrapped up in a
# neat little function call.
from django.template import Context
from django.views.generic import (CreateView,DetailView,ListView)
#app_name='articles'
from django.views.generic import (CreateView,DetailView,ListView)
#from  .forms import CreateArticle


