from django import forms
from .models import OfertaPracy

class OfertaPracyForm(forms.ModelForm):
    class Meta:
        model = OfertaPracy
        fields = ['tytul', 'opis', 'miejsce', 'wynagrodzenie', 'stanowisko', 'wymagania']
