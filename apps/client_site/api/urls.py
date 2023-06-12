from django.urls import path
from django.conf import settings
from .views import booking, contact


urlpatterns = [
    path('booking/', booking, name='booking'),
    path('contact-form/', contact, name='contact'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
