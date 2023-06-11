from django.urls import path
from django.conf import settings
from .views import home, about_us, contact_us, appointment, booking, calendar


urlpatterns = [
    path('', home, name="home"),
    path('about-us/', about_us, name="about_us"),
    path('contact-us/', contact_us, name="contact_us"),
    path('appointment/', appointment, name="appointment"),
    path('booking/', booking, name="booking"),
    path('calendar/', calendar, name="calendar"),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
