from django import forms
from mysite.audio.models import Audiofl


class AudioflForm(forms.ModelForm):
    class Meta:
        model = Audiofl
        fields = ('description', 'fl', )
        widgets = {'fl': forms.HiddenInput()}
