from django import forms
from .models import (
    Administrator,
    Aplikacja,
    Komentarz,
    Odpowiedz,
    Odpowiedznapytanieotwarte,
    Odpowiedznapytaniezamkniete,
    Ofertapracy,
    Pracodawca,
    Pracownik,
    PracownikZainteresowanie,
    Pytanieotwarte,
    Pytaniezamkniete,
    Stanuzytkownika,
    Statusaplikacji,
    Test,
    Typtestu,
    Uzytkownik,
    Zainteresowanie,
    ZainteresowanieOfertapracy,
)

class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = '__all__'


class AplikacjaForm(forms.ModelForm):
    class Meta:
        model = Aplikacja
        exclude = ['id']


class KomentarzForm(forms.ModelForm):
    class Meta:
        model = Komentarz
        exclude = ['id']


class OdpowiedzForm(forms.ModelForm):
    class Meta:
        model = Odpowiedz
        exclude = ['id']


class OdpowiedzNaPytanieOtwarteForm(forms.ModelForm):
    class Meta:
        model = Odpowiedznapytanieotwarte
        exclude = ['id']


class OdpowiedzNaPytanieZamknieteForm(forms.ModelForm):
    class Meta:
        model = Odpowiedznapytaniezamkniete
        exclude = ['id']


class OfertaPracyForm(forms.ModelForm):
    class Meta:
        model = Ofertapracy
        exclude = ['id', 'pracodawcauzytkownikid', 'testid']


class PracodawcaForm(forms.ModelForm):
    class Meta:
        model = Pracodawca
        exclude = ['uzytkownikid']


class PracownikForm(forms.ModelForm):
    class Meta:
        model = Pracownik
        exclude = ['uzytkownikid']


class PracownikZainteresowanieForm(forms.ModelForm):
    class Meta:
        model = PracownikZainteresowanie
        exclude = ['zainteresowanieid', 'pracownikuzytkownikid']


class PytanieOtwarteForm(forms.ModelForm):
    class Meta:
        model = Pytanieotwarte
        exclude = ['id']


class PytanieZamknieteForm(forms.ModelForm):
    class Meta:
        model = Pytaniezamkniete
        exclude = ['id']


class StanUzytkownikaForm(forms.ModelForm):
    class Meta:
        model = Stanuzytkownika
        fields = '__all__'


class StatusAplikacjiForm(forms.ModelForm):
    class Meta:
        model = Statusaplikacji
        fields = '__all__'


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        exclude = ['id']


class TypTestuForm(forms.ModelForm):
    class Meta:
        model = Typtestu
        fields = '__all__'


class UzytkownikForm(forms.ModelForm):
    class Meta:
        model = Uzytkownik
        exclude = ['id', 'stanuzytkownikaid']
        widgets = {
            'nazwauzytkownika': forms.TextInput(attrs={'required': True}),
            'email': forms.TextInput(attrs={'required': True}),
            'haslo': forms.PasswordInput(attrs={'required': True})
        }


class ZainteresowanieForm(forms.ModelForm):
    class Meta:
        model = Zainteresowanie
        exclude = ['id']


class ZainteresowanieOfertaPracyForm(forms.ModelForm):
    class Meta:
        model = ZainteresowanieOfertapracy
        exclude = ['ofertapracyid', 'zainteresowanieid']