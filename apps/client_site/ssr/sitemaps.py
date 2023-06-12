from django.contrib import sitemaps
from django.urls import reverse
# from datetime import datetime, timezone


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "always"

    def items(self):
        return ["home", "contact_us", "about_us"]

    def location(self, item):
        return reverse(item)

    # def lastmod(self, obj):
    #     return "2023-06-12 00:00 +00:00"
