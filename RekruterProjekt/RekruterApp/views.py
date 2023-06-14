from django.shortcuts import render
from django.db import connection
from django.contrib import messages
from .forms import OfertaPracyForm, UzytkownikForm, PracodawcaForm, PracownikForm, PytanieOtwarteForm, OdpowiedzNaPytanieOtwarteForm
from .models import Stanuzytkownika, Pracodawca, Pracownik, Test, Typtestu,\
    Pytanieotwarte, Odpowiedznapytanieotwarte, Ofertapracy

def index(request):
    return render(request, "RekruterApp/index.html")


def rejestracja(request):
    form = UzytkownikForm()
    pracodawca_form = PracodawcaForm()
    pracownik_form = PracownikForm()

    if request.method == 'POST':
        if 'zarejestruj' in request.POST:
            form = UzytkownikForm(request.POST)
            if form.is_valid():
                stan_uzytkownika = Stanuzytkownika.objects.create()
                uzytkownik = form.save(commit=False)
                uzytkownik.stanuzytkownikaid = stan_uzytkownika
                uzytkownik.save()
                wybor = request.POST.get("wybor")
                if wybor == "pracodawca":
                    pracodawca = Pracodawca.objects.create(
                        uzytkownikid=uzytkownik,
                        nazwafirmy=request.POST.get("nazwafirmy"),
                        glownasiedziba=request.POST.get("glownasiedziba"),
                        numerkontaktowy=request.POST.get("numerkontaktowy"),
                        branża=request.POST.get("branza")
                    )
                    return oferty(request)

                elif wybor == "pracownik":
                    pracownik = Pracownik.objects.create(
                        uzytkownikid=uzytkownik,
                        listmotywacyjny=request.POST.get("listmotywacyjny"),
                        cv=request.POST.get("cv")
                    )
                    return oferty(request)

    return render(request, "RekruterApp/profil.html", {"uzytkownik": form, "pracownik": pracownik_form,
                                                       "pracodawca": pracodawca_form})



def oferty(request):
    with connection.cursor() as cursor:
        query = "SELECT id,TytulOferty, SUBSTRING_INDEX(OpisOferty, ' ', 15)" \
                " AS 'Krótki opis' FROM ofertapracy limit 10"
        cursor.execute(query)
        result = cursor.fetchall()

    context = {
        'jobs': result,
    }
    return render(request, 'RekruterApp/oferty.html', context)

def oferty_testy(request, id_oferty):
    oferta = Ofertapracy.objects.get(id=id_oferty)
    with connection.cursor() as cursor:
        query = f"SELECT TytulOferty, OpisOferty  from OfertaPracy where id = {oferta.id}"
        cursor.execute(query)
        result = cursor.fetchall()

    odp_form = OdpowiedzNaPytanieOtwarteForm()
    pyt_form = OdpowiedzNaPytanieOtwarteForm()
    context = {
        'odp_form': odp_form,
        'pyt_form': pyt_form,
        'oferta': result
    }
    return render(request, 'RekruterApp/oferty_testy.html', context)



def dodaj_oferte(request):
    if request.method == 'POST':
        if 'dodaj' in request.POST:
            form = OfertaPracyForm(request.POST)
            pytanie = request.POST.get("question[]")
            pytania = request.POST.getlist("question[]")
            odpowiedzi = request.POST.getlist("answer[]")
            if len(pytanie) > 0:
                typ_testu = Typtestu.objects.create()
                test = Test.objects.create(
                    typtestuid=typ_testu
                )
                for i, j in zip(pytania, odpowiedzi):
                    pytania_otwarte = Pytanieotwarte.objects.create(
                        testid=test,
                        trescpytania=i
                    )
                    odpowiedzi_otwarte = Odpowiedznapytanieotwarte.objects.create(
                        pytanieotwarteid=pytania_otwarte,
                        trescodpowiedzinapytanie=j
                    )
                oferta_pracy = Ofertapracy.objects.create(
                    testid=test,
                    tytuloferty=request.POST.get("tytuloferty"),
                    opisoferty=request.POST.get("opisoferty")
                )
                return oferty(request)  # Przekierowanie na stronę z listą ofert (ustaw odpowiednią nazwę widoku)
            else:
                form.save()
                return oferty(request)
        else:
            form = OfertaPracyForm()
    else:
        form = OfertaPracyForm()

    return render(request, 'RekruterApp/dodaj.html', {"form": form})


# Create your views here.
