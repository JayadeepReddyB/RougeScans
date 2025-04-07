from django import forms
from .models import Manga,Chapter,ChapterImage
from django.forms import ModelForm,TextInput,Textarea,ClearableFileInput

class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = [
            'name',
            'desc',
            'pic'
        ]

        widgets = {
            'name' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width:400px',
                'placeholder': 'Manga',
            }),
            'desc': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width:400px',
                'placeholder': 'Description',
            }),
            'pic': forms.ClearableFileInput(attrs={
                'class': "form-control",
                'style': 'max-width:400px',
                
            })
        }

class EditChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = [
            'title',
            'chapter_number',
            'release_date'
        ]

        widgets = {

            'title': forms.TextInput(attrs={
            'class': "form-control",
            'style': 'max-width:230px',
            'placeholder': 'Chapter Title',
            }),
           'chapter_number': forms.NumberInput(attrs={
           'class': "form-control",
           'style': 'max-width:230px',
            'placeholder': 'Chapter Number',
            }),
           'release_date': forms.DateInput(attrs={
           'class': "form-control",
          'style': 'max-width:230px',
          'placeholder': 'YYYY-MM-DD',
          'type': 'date',  # Enables HTML5 date picker
           }),
        }

class AddChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = [
            'manga',
            'title',
            'chapter_number',
            'release_date'
        ]

        widgets = {
            'manga': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width:230px',
            }),
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width:230px',
                'placeholder': 'Chapter Title',
            }),
            'chapter_number': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width:230px',
                'placeholder': 'Chapter Number',
            }),
            'release_date': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width:230px',
                'placeholder': 'YYYY-MM-DD',
                'type': 'date',
            }),
        }


class ChapterImageForm(forms.ModelForm):
    class Meta:
        model = ChapterImage
        fields = [
            'id',
            'chapter',
            'image'
        ]

        widgets = {
            
            'id': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width:230px',
                'placeholder': 'Chapter Number',
            }),
            'chapter': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width:230px',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': "form-control",
                'style': 'max-width:400px'
            }),
        }

class EditChapterImageForm(forms.ModelForm):
    class Meta:
        model = ChapterImage
        fields = [
            'chapter',
            'image'
        ]

        widgets = {
                'chapter': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width:230px',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': "form-control",
                'style': 'max-width:400px'
            }),
        }