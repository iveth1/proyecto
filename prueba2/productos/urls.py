from django.http.response import HttpResponse
from django.template import context
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns =[
    path('',views.home, name='home'),
    path('productos/', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/new/', views.new_usuario, name="new_usuarios"),
    path('catalogo/iniciar/', LoginView.as_view(template_name='productos/iniciar_sesion.html'), name="iniciar_sesion"),
    #path('catalogo/iniciarout/', LogoutView.as_view(template_name='iniciar_sesion'), name="iniciar_sesion"),
]

