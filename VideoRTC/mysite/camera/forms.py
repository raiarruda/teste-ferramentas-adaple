from django import forms
from .models import db_video


class UploadFileForm(forms.ModelForm): 
   
    video_file = forms.FileField()
    class Meta:
        model = db_video
        fields = ['video', ]