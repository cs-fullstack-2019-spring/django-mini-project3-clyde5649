from django import forms
from .models import TimeCard

# shows all the fields on my page

class TimeCardForm(forms.ModelForm):
    class Meta():
        model = TimeCard
        fields = ['teachername','school','subject','hours','dateofwork']