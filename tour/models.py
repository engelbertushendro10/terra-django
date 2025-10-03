from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.utils import timezone
from meta.models import ModelMeta
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
import uuid
import os


def upload_kapal_thumbnail(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('kapal_images/', filename)


def upload_paket_thumbnail(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('paket_images/', filename)


class KategoriPaket (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# class paket


class Paket(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    paket_category = models.ForeignKey(KategoriPaket, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=upload_paket_thumbnail)
    content = RichTextUploadingField()
    tanggal = models.DateField(default=timezone.now)

    _metadata = {
        'title': title,
        'description': 'get_meta_description',
        'image': 'get_meta_image',
        'keywords': 'get_meta_keywords',
    }

    def get_meta_description(self):
        return (
            f"Jelajahi keindahan Labuan Bajo bersama {self.title} – "
            f"{self.paket_category.title.lower()} eksklusif yang mencakup Komodo, Pulau Padar, dan pengalaman tak terlupakan "
            f"dengan kapal phinisi terbaik."
        )

    def get_meta_keywords(self):
        return [
            self.title,
            self.paket_category.title,
            "paket tour labuan bajo",
            "paket wisata komodo",
            "open trip labuan bajo",
            "tour pulau padar",
            "paket liburan ke labuan bajo",
            "kapal phinisi labuan bajo",
            "trip komodo island",
            "wisata alam labuan bajo",
            "honeymoon labuan bajo",
            "paket snorkeling labuan bajo",
            "jadwal tour labuan bajo",
            "promo paket wisata komodo",
            "berita wisata labuan bajo",
            f"{self.title.lower()} labuan bajo",
            f"{self.paket_category.title.lower()} komodo island",
            "paket tour 3 hari 2 malam labuan bajo",
            "private trip labuan bajo",
            "open trip komodo island",
            "kapal wisata terbaik labuan bajo"
        ]

    def get_meta_image(self):
        return self.thumbnail.url if self.thumbnail else None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Kapal(models.Model):
    nama = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    kapal_kategori = models.ForeignKey(KategoriPaket, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=upload_kapal_thumbnail)
    content = RichTextUploadingField()
    tanggal = models.DateField(default=timezone.now)

    _metadata = {
        'title': nama,
        'description': 'get_meta_description',
        'image': 'get_meta_image',
        'keywords': 'get_meta_keywords'
    }

    def get_meta_description(self):
        return self.content[:150]

    def get_meta_keywords(self):
        return [
            self.nama,
            self.kapal_kategori.title,
            f"paket tour labuan bajo {self.nama.lower()}",
            "paket wisata labuan bajo",
            "open trip labuan bajo",
            "sewa kapal labuan bajo",
            "tour komodo island",
            "kapal phinisi labuan bajo",
            "honeymoon labuan bajo",
            "liburan ke labuan bajo",
            "trip murah labuan bajo",
            "jadwal tour labuan bajo",
            "destinasi wisata labuan bajo",
            "kapal terbaik labuan bajo",
            "paket snorkeling labuan bajo"
        ]

    def get_meta_image(self):
        return self.thumbnail.url if self.thumbnail else None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama


class FotoGaleri(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    konten = GenericForeignKey('content_type', 'object_id')

    image = models.ImageField(upload_to='galeri/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Foto untuk {self.konten}"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,  unique=True)
    content = RichTextUploadingField()
    tanggal = models.DateField(default=timezone.now)
    thumbnail = models.ImageField(upload_to='blog_foto/')
    _metadata = {
        'title': title,
        'description': 'get_meta_description',
        'image': 'get_meta_image',
        'keywords': 'get_meta_keywords',
    }

    def get_meta_description(self):
        return self.content[:150]

    def get_meta_keywords(self):
        return [
            self.title,
        ]

    def get_meta_image(self):
        return self.thumbnail.url if self.thumbnail else None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
