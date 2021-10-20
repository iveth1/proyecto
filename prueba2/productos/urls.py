#from django import template
from django.conf.urls import static
from django.http.response import HttpResponse
from django.template import context
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

#urlpatterns = [...] #aquí irían mis direcciones y al final
#urlpatterns += staticfiles(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns =[
    path('',views.home, name='home'),
    path('productos/', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/new/', views.new_usuario, name="new_usuarios"),
    path('catalogo/iniciar/', LoginView.as_view(template_name='productos/iniciar_sesion.html'), name="iniciar_sesion"),
    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    path('catalogo/producto/', views.producto, name='producto'),
    path('catalogo/bases/', views.bases, name='bases'),
    path('catalogo/iluminador/', views.iluminador, name='iluminador'),
    path('catalogo/pestanina/', views.pestanina, name='pestanina'),
    path('catalogo/sombras/', views.sombras, name='sombras'),
    path('catalogo/delineador/', views.delineador, name='delineador'),
    path('catalogo/lapiz/', views.lapiz, name='lapiz'),
    path('catalogo/rubor/', views.rubor, name='rubor'),
    path('catalogo/brillo/', views.brillo, name='brillo'),
    path('catalogo/corrector/', views.corrector, name='corrector'),
]

