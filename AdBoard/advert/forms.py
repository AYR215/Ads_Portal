from django import forms
from django.forms import ModelForm, Form
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AdsForm(ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Ad
        fields = '__all__'


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['resp_post', 'resp_user', 'resp_text']
