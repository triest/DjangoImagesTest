from django.http import Http404
from django.shortcuts import render, redirect
from . import forms
from .forms import ImageForm
from .models import Image, Comment


def ImagesListView(request):
    template_name = 'articles/article_list.html'
    # queryset = Article.objects.all().order_by('-date')
    images = Image.objects.all().order_by('-date')

    return render(request, 'images/images_list.html', {'images': images})
    # return HttpResponse('homepage')


def ImageCreate(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=True)
            instance.save()
            return ImagesListView(request)

    else:
        form = ImageForm()
        return render(request, 'images/create.html', {'form': form})


def DetailView(request, pk):
    try:
        image = Image.objects.get(id=pk);
    except Image.DoesNotExist:
        raise Http404

    comments = image.comment_set.all();

    if request.method == 'POST':
        form = forms.CommentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=True)
            instance.image_id = pk;
            instance.save()

    form = forms.CommentForm()

    return render(request, 'images/image_view.html', {'image': image, 'comments': comments, 'form': form})


def CommentDelete(request, pk, image_pk):
    try:
        comment = Comment.objects.get(id=pk)
    except Comment.DoesNotExist:
        raise Http404
    comment.delete()

    return DetailView(request, image_pk)


def CommentEdit(request, pk,comment_pk):
    comment = Comment.objects.get(id=comment_pk)
    #form = RegisterForm(request.POST)  # if no files
    comment.title =request.POST.get("title2", "")
    comment.save()

    return DetailView(request, pk)
