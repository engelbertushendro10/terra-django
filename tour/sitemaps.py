from django.contrib.sitemaps import Sitemap
from .models import News

class PaketWisataSitemap(Sitemap):
    def items(self):
        return News.objects.all()