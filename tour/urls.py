from django.urls import path
from .views import paket_list, paket_detail, blog, blog_detail

# urlpatterns = [
#     path('', paket_list, name='paket_list'),
#     path('<slug:slug>/', paket_detail, name='paket_detail'),
#     path('blog/', blog, name='blog'),
#     path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
# ]

# from django.urls import path
# from . import views

urlpatterns = [
    path('', paket_list, name='paket_list'),
    path('blog/', blog, name='blog'),  # Pastikan ini sebelum paket_detail
    # path('<slug:slug>/', paket_detail, name='paket_detail'),
    path('blog/<slug:slug>/', blog_detail,
         name='blog_detail'),  # URL untuk detail blog
]
