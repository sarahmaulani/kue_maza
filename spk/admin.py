# spk/admin.py
from django.contrib import admin
from .models import UserProfile, Produk, Kriteria, NilaiProduk, Periode

# UserProfile - HAPUS 'telepon' dari list_display
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']  # ← HANYA 'user' saja
    # 'telepon' tidak ada di model, JANGAN dipakai

@admin.register(Periode)
class PeriodeAdmin(admin.ModelAdmin):
    list_display = ['id','nama_periode', 'tahun']

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ['nama']

@admin.register(Kriteria)
class KriteriaAdmin(admin.ModelAdmin):
    list_display = ['nama']

@admin.register(NilaiProduk)
class NilaiProdukAdmin(admin.ModelAdmin):
    list_display = ['produk', 'kriteria', 'nilai']
