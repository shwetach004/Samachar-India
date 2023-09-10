from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('gallery/',views.gallery),
    path('video/',views.video),
    path('news/',views.news),
    path('',views.index),
    path('login/',views.login),
    path('viewnews/',views.viewnews),
    path('details/',views.ndetails),
    path('vdetail/',views.vdetail)




]

