from django.conf.urls import url
from .views import *
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [

                  url(r'^$', views.index, name='index'),
                  url(r'^(?P<id>\d+)/$', views.post_detail, name='PostDetail'),
                  path('add_post/', AddPost.as_view(), name='AddPost'),

                  # url(r'^search-form/$', views.search_form),
                  # url(r'^search/$', views.search),

                  # url(r'^test/$', views.test_view, name='test'),

              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
