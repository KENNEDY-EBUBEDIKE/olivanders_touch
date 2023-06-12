from django.contrib import sitemaps
from django.urls import reverse
import datetime
from pytz import timezone


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "always"

    def items(self):
        return ["home", "contact_us", "about_us"]

    def location(self, item):
        return reverse(item)

    def lastmod(self, obj):
        return datetime.datetime.now(tz=timezone('Africa/Lagos')).date()
