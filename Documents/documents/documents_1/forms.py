from django import forms
from .models import Document


# from .models import Document


class DocumentsForm(forms.ModelForm):
    images = forms.ImageField(label='Фото документа', widget=forms.ClearableFileInput(attrs={'multiple': True, "class":"mybottom"}))

    class Meta:
        model = Document
        widgets = {
            'dateCreate': forms.DateInput(attrs={'type': 'date'}),
        }
        # {
        #     'author': request.user.username
        # }

        fields = ['author', 'title', 'category', 'textDocument', 'number', 'dateCreate', 'images']


class DocumentForm(forms.ModelForm):
    # images = forms.ImageField(label='Фото', widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Document
        widgets = {
            'dateCreate': forms.DateInput(attrs={'type': 'date'}),
        }

        fields = ['title', 'category', 'textDocument', 'number', 'dateCreate']
