from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OfertaPracyForm

def index(request):
    return render(request, "RekruterApp/index.html")

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
        form = OfertaPracyForm(request.POST)
        if form.is_valid():
            # Utwórz nowy obiekt OfertaPracy na podstawie danych z formularza
            form.save()
            messages.success(request, 'Oferta pracy została dodana.')
            return oferty(request)  # Przekierowanie na stronę z listą ofert
        else:
            messages.error(request, 'Wystąpił błąd. Proszę wypełnić poprawnie formularz.')
    else:
        form = OfertaPracyForm()

    context = {'form': form}
    return render(request, 'RekruterApp/dodaj.html', context)

# Create your views here.
