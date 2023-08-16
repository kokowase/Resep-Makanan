from django.contrib import admin
from .models import Resep,Bahan,Kategori
# Register your models here.

admin.site.register(Kategori)
admin.site.register(Bahan)
admin.site.register(Resep)