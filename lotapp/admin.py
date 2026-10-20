from django.contrib import admin
from .models import Samolot,Linia,Marka,Przeznaczenie,Czesc,Zabezpieczenia,Typ,ModelNazwa

custom_admin_site = admin.AdminSite(name="custom_admin")

custom_admin_site.site_header = "Mój własny panel"

@admin.register(Samolot,Linia,Marka,Przeznaczenie,Czesc,Zabezpieczenia,Typ,ModelNazwa, site = custom_admin_site)
class SamolotAdmin(admin.ModelAdmin):
    pass