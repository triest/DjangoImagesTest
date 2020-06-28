from django import forms
from django.core.files.images import get_image_dimensions

from . import models


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ['title', 'image']
        name = forms.CharField(label='Title', max_length=100)
        image = forms.CharField(label='Image', max_length=100)

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title:
            return forms.ValidationError("title is requared")
        else:
            return title

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            raise forms.ValidationError("No image!")
        else:
            return image


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['title']
        title = forms.CharField(label='Comment text', max_length=100)

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title:
            return forms.ValidationError("title is requared")
        else:
            return title
