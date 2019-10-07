from django.conf.urls import url
from .views import *
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [

                  url(r'^$', views.index_view, name='index'),

              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
