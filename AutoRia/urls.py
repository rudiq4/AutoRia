from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'AutoRia'

urlpatterns = [
                  url(r'^admin/', admin.site.urls, name='admin'),
                  url(r'^chaining/', include('smart_selects.urls')),
                  url(r'^', include('main.urls')),
                  url(r'^', include('registration.urls')),

              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
