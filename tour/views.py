from django.shortcuts import render, get_object_or_404
from .models import Paket, KategoriPaket, Kapal, FotoGaleri, Blog
from django.contrib.contenttypes.models import ContentType


def paket_list(request):
    kategori_list = Paket.objects.all()
    kategori_slug = request.GET.get('kategori')

    if kategori_slug:
        paket_list = Paket.objects.filter(
            paket_category__slug=kategori_slug).order_by('-tanggal')
    else:
        paket_list = Paket.objects.all().order_by('-tanggal')

    kapal_display = Kapal.objects.all().order_by('-tanggal')[:3]

    blog_display = Blog.objects.all().order_by('-tanggal')[:6]
    context = {
        'paket_list': paket_list,
        'kategori_list': kategori_list,
        'kapal_display': kapal_display,
        'blog_display': blog_display
    }

    # Ambil semua foto untuk setiap paket
    for paket in paket_list:
        paket.foto_galeri = FotoGaleri.objects.filter(
            content_type=ContentType.objects.get_for_model(Paket),
            object_id=paket.id
        )
    for kapal in kapal_display:
        kapal.foto_galeri = FotoGaleri.objects.filter(
            content_type=ContentType.objects.get_for_model(Kapal),
            object_id=kapal.id
        )
    return render(request, 'tour/paket_list.html', context)


def paket_detail(request, slug):
    paket = get_object_or_404(Paket, slug=slug)
    kategori_list = Paket.objects.all()
    context = {
        'paket': paket,
        'kategori_list': kategori_list
    }
    return render(request, 'tour/paket_detail.html', context)


def blog(request):
    blog = Blog.objects.all()
    return render(request, 'tour/blog.html', {'blogs': blog})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'tour/blog_detail.html', {'blogs': blog})
