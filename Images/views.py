from django.shortcuts import render, redirect
from . import forms
from .forms import ImageForm
from .models import Image


def ImagesListView(request):
    template_name='articles/article_list.html'
    #queryset = Article.objects.all().order_by('-date')
    images=Image.objects.all().order_by('-date')

    return render(request,'images/images_list.html',{'images':images})
    #return HttpResponse('homepage')

def ImageCreate(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST,request.FILES )
        if form.is_valid():
            instance = form.save(commit=True)
            instance.save()
            return ImagesListView(request)

    else:
        form = ImageForm()
        return render(request, 'images/create.html', {'form': form})

def DetailView(request,pk):
    images = Image.objects.get(id=pk)
    return render(request, 'images/image_view.html', {'image': images})