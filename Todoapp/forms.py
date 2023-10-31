#task updating movie details
from django import forms
from .models import Tsk
class form_tsk(forms.ModelForm):
    class Meta:
        model=Tsk
        fields=['task','priority','date']