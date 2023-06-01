from django.shortcuts import render
from django.db import connection
from django.contrib import messages
from .forms import OfertaPracyForm, UzytkownikForm, PracodawcaForm, PracownikForm

def index(request):
    return render(request, "RekruterApp/index.html")


def rejestracja(request):
    form = UzytkownikForm()
    pracodawca_form = PracodawcaForm()
    pracownik_form = PracownikForm()


    if request.method == 'POST':
        if 'zarejestruj' in request.POST:
            form = UzytkownikForm(request.POST)
            email = request.POST.get("email")
            if form.is_valid():
                with connection.cursor() as cursor:
                    query = "SELECT COUNT(*) FROM Uzytkownik WHERE Email = %s"
                    cursor.execute(query, [email])
                    result = cursor.fetchone()[0]
                    if result > 0:
                        messages.error(request, 'Dany email jest już w bazie danych, wprowadź inny.')
                    else:
                        #form.save()
                        print("Zapisano")

        if 'wyslij' in request.POST:
            wybor = request.POST.get("wybor")
            if wybor == "pracodawca":
                pracodawca_form = PracodawcaForm(request.POST)
                if pracodawca_form.is_valid():
                    #pracodawca_form.save()
                    return oferty(request)
            elif wybor == "pracownik":
                pracownik_form = PracownikForm(request.POST)
                if pracownik_form.is_valid():
                    #pracownik_form.save()
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
