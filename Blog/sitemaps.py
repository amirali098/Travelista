from django.contrib import sitemaps
from django.urls import reverse
from django.utils import timezone

from .models import posts


class BlogViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return posts.objects.filter(published_date__lte=timezone.now(), status=True)

    def lastmod(self, obj):
        return obj.published_date

    def location(self, item):
        return   reverse('blogsingle',kwargs={'pid':item.id})