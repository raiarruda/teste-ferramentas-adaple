from django import forms
from .models import MyModel
from tinymce import TinyMCE


class MyForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))

    class Meta:
        model = MyModel
        fields = ('content',)