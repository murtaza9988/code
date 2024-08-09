from django import forms
from . models import *

class students_data(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'