from django.shortcuts import render
from django.contrib import messages
from .forms import OfertaPracyForm, UzytkownikForm

def index(request):
    return render(request, "RekruterApp/index.html")

def rejestracja(request):
    form = UzytkownikForm()
    if request.method == 'POST':
        if 'zarejestruj' in request.POST:
            form = UzytkownikForm(request.POST)
            form.save()
            return login(request)
        else:
            messages.error(request, 'Dany email jest już w bazie danych, wprowadź inny.')
    return render(request, "RekruterApp/rejestracja.html", {"form": form})


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
        'jobs': jobs
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
