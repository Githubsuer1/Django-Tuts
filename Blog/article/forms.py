from .models import Article 
from django.forms import ModelForm
from django import forms


class createPostForm(ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={
        "class":"p-3 rounded mt-5 w-auto",
        "type":"text",
        "placeholder":"Enter title.."
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class":"p-3 rounded mt-4 border-2 w-auto",
        "type":"file",
    }))

    class Meta:
        model = Article 
        fields = ["title","image"]

class editPostForm(ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={
        "class":"p-3 rounded mt-5 w-auto ",
        "type":"text",
        "placeholder":"Enter title.."
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class":"p-3 rounded mt-4 border-2 w-auto ",
        "type":"file",
    }))

    class Meta:
        model = Article 
        fields = ["title","image"]