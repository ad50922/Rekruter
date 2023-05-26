from django.db import models

class OfertaPracy(models.Model):
    tytul = models.CharField(max_length=100)
    opis = models.TextField()
    miejsce = models.CharField(max_length=100)
    wymagania = models.CharField(max_length=100)
    stanowisko = models.CharField(max_length=100)
    wynagrodzenie = models.CharField(max_length=100)
    test = models.BooleanField(default=False)

    def __str__(self):
        return self.tytul

