from django.urls import path
from . import views

app_name = 'leo_stronda_app'  # Namespace para evitar conflitos

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('contatos/', views.contatos, name='contatos'),
    path('add-produto/', views.add_produto, name='add_produto'),
]