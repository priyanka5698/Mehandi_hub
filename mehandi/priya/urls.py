from django.conf.urls import url
from . import views

urlpatterns = [
         url(r'^$', views.index, name='index'),
         url(r'^home/$', views.home, name='home'),
        url(r'^aboutme/$', views.about, name='about'),
        url(r'^services/$', views.service, name='service'),
        url(r'^Mygellery/$', views.gallery, name='gallery'),
        url(r'^Myblog/$', views.blog, name='blog'),
    url(r'^reviews/$', views.review, name='review'),
    url(r'^contactme/$', views.contact, name='contact'),
    url(r'^restuarant/$', views.register, name='register'),


    ]