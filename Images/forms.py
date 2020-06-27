
from django import forms
from . import models


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ['title','image']
        name = forms.CharField(label='Title', max_length=100)
        image = forms.CharField(label='Image', max_length=100)


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['title']
        title = forms.CharField(label='Title', max_length=100)
