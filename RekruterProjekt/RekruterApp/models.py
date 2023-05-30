# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    uzytkownikid = models.OneToOneField('Uzytkownik', models.DO_NOTHING, db_column='UzytkownikID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrator'


class Aplikacja(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pracownikuzytkownikid = models.ForeignKey('Pracownik', models.DO_NOTHING, db_column='PracownikUzytkownikID')  # Field name made lowercase.
    ofertapracyid = models.ForeignKey('Ofertapracy', models.DO_NOTHING, db_column='OfertaPracyID')  # Field name made lowercase.
    statusaplikacjiid = models.ForeignKey('Statusaplikacji', models.DO_NOTHING, db_column='StatusAplikacjiID')  # Field name made lowercase.
    listmotywacyjny = models.CharField(db_column='ListMotywacyjny', max_length=1023, blank=True, null=True)  # Field name made lowercase.
    cv = models.TextField(db_column='CV', blank=True, null=True)  # Field name made lowercase.
    datawyslaniaaplikacji = models.DateField(db_column='DataWyslaniaAplikacji', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aplikacja'


class Komentarz(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    uzytkownikid2 = models.ForeignKey('Uzytkownik', models.DO_NOTHING, db_column='UzytkownikID2')  # Field name made lowercase.
    uzytkownikid = models.ForeignKey('Uzytkownik', models.DO_NOTHING, db_column='UzytkownikID', related_name='komentarz_uzytkownikid_set')  # Field name made lowercase.
    tresckomentarza = models.CharField(db_column='TrescKomentarza', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'komentarz'


class Odpowiedz(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pytaniezamknieteid = models.ForeignKey('Pytaniezamkniete', models.DO_NOTHING, db_column='PytanieZamknieteID')  # Field name made lowercase.
    trescodpowiedzi = models.CharField(db_column='TrescOdpowiedzi', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'odpowiedz'


class Odpowiedznapytanieotwarte(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pytanieotwarteid = models.ForeignKey('Pytanieotwarte', models.DO_NOTHING, db_column='PytanieOtwarteID')  # Field name made lowercase.
    aplikacjaid = models.ForeignKey(Aplikacja, models.DO_NOTHING, db_column='AplikacjaID')  # Field name made lowercase.
    trescodpowiedzinapytanie = models.CharField(db_column='TrescOdpowiedziNaPytanie', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'odpowiedznapytanieotwarte'


class Odpowiedznapytaniezamkniete(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pytaniezamknieteid = models.ForeignKey('Pytaniezamkniete', models.DO_NOTHING, db_column='PytanieZamknieteID')  # Field name made lowercase.
    aplikacjaid = models.ForeignKey(Aplikacja, models.DO_NOTHING, db_column='AplikacjaID')  # Field name made lowercase.
    numerodpowiedzi = models.IntegerField(db_column='NumerOdpowiedzi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'odpowiedznapytaniezamkniete'


class Ofertapracy(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pracodawcauzytkownikid = models.ForeignKey('Pracodawca', models.DO_NOTHING, db_column='PracodawcaUzytkownikID')  # Field name made lowercase.
    testid = models.ForeignKey('Test', models.DO_NOTHING, db_column='TestID', blank=True, null=True)  # Field name made lowercase.
    tytuloferty = models.CharField(db_column='TytulOferty', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opisoferty = models.CharField(db_column='OpisOferty', max_length=2047, blank=True, null=True)  # Field name made lowercase.
    datadodaniaoferty = models.DateField(db_column='DataDodaniaOferty', blank=False, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ofertapracy'


class Pracodawca(models.Model):
    uzytkownikid = models.OneToOneField('Uzytkownik', models.DO_NOTHING, db_column='UzytkownikID', primary_key=True)  # Field name made lowercase.
    nazwafirmy = models.CharField(db_column='NazwaFirmy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    glownasiedziba = models.CharField(db_column='GlownaSiedziba', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numerkontaktowy = models.IntegerField(db_column='NumerKontaktowy')  # Field name made lowercase.
    branża = models.CharField(db_column='Branża', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pracodawca'


class Pracownik(models.Model):
    uzytkownikid = models.OneToOneField('Uzytkownik', models.DO_NOTHING, db_column='UzytkownikID', primary_key=True)  # Field name made lowercase.
    listmotywacyjny = models.CharField(db_column='ListMotywacyjny', max_length=1023, blank=True, null=True)  # Field name made lowercase.
    cv = models.IntegerField(db_column='CV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pracownik'


class PracownikZainteresowanie(models.Model):
    zainteresowanieid = models.OneToOneField('Zainteresowanie', models.DO_NOTHING, db_column='ZainteresowanieID', primary_key=True)  # Field name made lowercase. The composite primary key (ZainteresowanieID, PracownikUzytkownikID) found, that is not supported. The first column is selected.
    pracownikuzytkownikid = models.ForeignKey(Pracownik, models.DO_NOTHING, db_column='PracownikUzytkownikID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pracownik_zainteresowanie'
        unique_together = (('zainteresowanieid', 'pracownikuzytkownikid'),)


class Pytanieotwarte(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    testid = models.ForeignKey('Test', models.DO_NOTHING, db_column='TestID', blank=True, null=True)  # Field name made lowercase.
    trescpytania = models.CharField(db_column='TrescPytania', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pytanieotwarte'


class Pytaniezamkniete(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    testid = models.ForeignKey('Test', models.DO_NOTHING, db_column='TestID', blank=True, null=True)  # Field name made lowercase.
    trescpytania = models.CharField(db_column='TrescPytania', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numerprawidlowejodpowiedzi = models.IntegerField(db_column='NumerPrawidlowejOdpowiedzi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pytaniezamkniete'


class Stanuzytkownika(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stanuzytkownika'


class Statusaplikacji(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statusaplikacji'


class Test(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    typtestuid = models.ForeignKey('Typtestu', models.DO_NOTHING, db_column='TypTestuID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test'


class Typtestu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typtestu'


class Uzytkownik(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    stanuzytkownikaid = models.ForeignKey(Stanuzytkownika, models.DO_NOTHING, db_column='StanUzytkownikaID', default=1)  # Field name made lowercase.
    nazwauzytkownika = models.CharField(db_column='NazwaUzytkownika', max_length=255, blank=True, null=True)  # Field name made lowercase.
    haslo = models.CharField(db_column='Haslo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    opis = models.CharField(db_column='Opis', max_length=1023, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uzytkownik'



class Zainteresowanie(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zainteresowanie'


class ZainteresowanieOfertapracy(models.Model):
    ofertapracyid = models.OneToOneField(Ofertapracy, models.DO_NOTHING, db_column='OfertaPracyID', primary_key=True)  # Field name made lowercase. The composite primary key (OfertaPracyID, ZainteresowanieID) found, that is not supported. The first column is selected.
    zainteresowanieid = models.ForeignKey(Zainteresowanie, models.DO_NOTHING, db_column='ZainteresowanieID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zainteresowanie_ofertapracy'
        unique_together = (('ofertapracyid', 'zainteresowanieid'),)
