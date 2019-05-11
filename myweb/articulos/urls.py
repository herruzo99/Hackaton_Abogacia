from django.urls import path

from . import views

urlpatterns = [
    path('oficial/', views.oficial, name='oficial'),
    path('sugerencia/', views.sugerencia, name='sugerencia'),
    path('registro/', views.registro, name='registro'),
    path('<int:articulo_id>/', views.articulo, name='articulo')

]