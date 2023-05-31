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

    context = {
        'pracownik': pracownik_form,
        'pracodawca': pracodawca_form,
        'form': form
    }

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
                    pracodawca_form.save()
                    return oferty(request)
            elif wybor == "pracownik":
                pracownik_form = PracownikForm(request.POST)
                if pracownik_form.is_valid():
                    #pracownik_form.save()
                    return oferty(request)

    return render(request, "RekruterApp/profil.html", context)

def login(request):
    if request.method == 'POST':
        if 'zaloguj' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Sprawdzenie poprawności danych logowania
            # kwerenda na sprawdzenie poprawnosci logowania
            if username == 'admin' and password == 'admin123':
                return oferty(request)
            else:
                # Nieprawidłowe dane logowania
                messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło.')

    return render(request, 'RekruterApp/logowanie.html')

def oferty(request):
    #kwerenda na wyswietlenie pierwszy 10 ofert
    jobs = [
        {'title': 'Oferta pracy 1', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'},
        {'title': 'Oferta pracy 2', 'description': 'Sed at justo sit amet elit bibendum tincidunt.'},
        {'title': 'Oferta pracy 3', 'description': 'Vestibulum eleifend nibh in mauris bibendum.'},
        {"qweqweqwe": "asdqweqwe"},
    ]

    context = {
        'jobs': jobs,
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
