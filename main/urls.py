from django.conf.urls import url
from .views import *
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [

                  url(r'^$', views.vehicle_list, name='vehicle_list'),
                  url(r'^carpage/$', views.carpage, name='carpage'),
                  # url(r'^search-form/$', views.search_form),
                  url(r'^search/$', views.search),



                  #url(r'^test/$', views.test_view, name='test'),


              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
