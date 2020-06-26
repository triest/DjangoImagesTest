from django.shortcuts import render, redirect
from . import forms
from .forms import ImageForm


def ImagesListView(request):
    return render(request,'images/images_list.html')
    #return HttpResponse('homepage')

def ImageCreate(request):

    form = ImageForm()
    return render(request, 'images/create.html', {'form': form})