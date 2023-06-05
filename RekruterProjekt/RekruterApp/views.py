from django.shortcuts import render
from django.db import connection
from django.contrib import messages
from .forms import OfertaPracyForm, UzytkownikForm, PracodawcaForm, PracownikForm
from .models import Stanuzytkownika, Pracodawca, Pracownik

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
                    print("JESTEM TUTAJJJJJJJJ")
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
        query = "SELECT TytulOferty, SUBSTRING_INDEX(OpisOferty, ' ', 15)" \
                " AS 'Krótki opis' FROM ofertapracy"
        cursor.execute(query)
        result = cursor.fetchall()

    context = {
        'jobs': result,
    }

    return render(request, 'RekruterApp/oferty.html', context)

def dodaj_oferte(request):
    if request.method == 'POST':
        if 'dodaj' in request.POST:
            form = OfertaPracyForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Oferta pracy została dodana.')
                return oferty(request)  # Przekierowanie na stronę z listą ofert (ustaw odpowiednią nazwę widoku)
            else:
                messages.error(request, 'Wystąpił błąd. Proszę wypełnić poprawnie formularz.')
        else:
            form = OfertaPracyForm()
    else:
        form = OfertaPracyForm()

    return render(request, 'RekruterApp/dodaj.html', {"form": form})


# Create your views here.
