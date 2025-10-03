from symtable import Class

from django.contrib import admin
from .models import KategoriPaket, Paket, Kapal, FotoGaleri, Blog
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.


class FotoGaleriInline(GenericTabularInline):  # Bisa juga pakai StackedInline
    # model = FotoGaleri
    # extra = 3  # Jumlah form kosong yang muncul
    # fields = ['image', 'caption']
    # readonly_fields = []
    # show_change_link = True
    model = FotoGaleri
    extra = 3  # Jumlah form kosong yang muncul
    fields = ['image', 'caption']


@admin.register(KategoriPaket)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Paket)
class NewsAdmin(admin.ModelAdmin):
    inlines = [FotoGaleriInline]
    list_display = ('title', 'paket_category', 'tanggal')
    inlines = [FotoGaleriInline]
    list_filter = ('paket_category', 'tanggal')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('tanggal',)


@admin.register(Kapal)
class kapalAdmin(admin.ModelAdmin):
    inlines = [FotoGaleriInline]
    list_display = ('nama', 'kapal_kategori', 'tanggal')
    search_fields = ('nama', 'kategori')
    prepopulated_fields = {'slug': ('nama',)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'tanggal')
    prepopulated_fields = {'slug': ('title',)}
