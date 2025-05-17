from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request, 'home.html')

def produtos(request):
    return render(request, 'produtos.html')


def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'meuapp/produtos.html', {'produtos': produtos})


def contatos(request):
    return render(request, 'contatos.html')