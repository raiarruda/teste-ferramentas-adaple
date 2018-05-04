from django import forms
from .models import db_video,MyModel

from ckeditor.widgets import CKEditorWidget

class UploadFileForm(forms.ModelForm): 
   
    video_file = forms.FileField()
    class Meta:
        model = db_video
        fields = ['nome', ]



class MyForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = MyModel
        fields = ('content',)