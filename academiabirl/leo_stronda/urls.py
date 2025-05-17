from django.urls import path
from . import views

app_name = 'leo_stronda'

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('contatos/', views.contatos, name='contatos'),
    # Adicione outras URLs conforme necessário
]
