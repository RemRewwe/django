from django.shortcuts import render, redirect
from .models import Login
from django.conf import settings
from .forms import LoginForm, ProfileForm, CadastroForm
import os

def home(request):
    return render(request, 'pro_final/home.html')

def login(request):
    login = Login.objects.filter(disponivel=True)
    return render(request, 'pro_final/login.html', {'logins': logins})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')
    return render(request, 'pro_final/cadastro.html')


def list_profile_pics(request):
    """
    Lista todas as imagens de perfil usando a OS Library.
    """
    pics_path = os.path.join(settings.MEDIA_ROOT, 'profile_pics')
    pictures = [f for f in os.listdir(pics_path) if f.endswith(('.jpg', '.png'))]
    return render(request, 'list_pics.html', {'pictures': pictures})


def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'pro_final/upload_profile.html', {'form': form})

def contato(request):
    """Página de contato (formulário)"""
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Salva a solicitação no banco
            solicitacao = form.save()

            # Envia email (opcional)
            try:
                send_mail(
                    subject=f'Nova solicitação: {solicitacao.assunto}',
                    message=f'''
                    Nova solicitação de contato recebida:

                Nome: {solicitacao.nome}
                Email: {solicitacao.email}
                Telefone: {solicitacao.telefone}
                Assunto: {solicitacao.assunto}

                Mensagem:
                {solicitacao.mensagem}
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@reformas.com',
                recipient_list=['contato@empresa.com'],  # Substitua pelo seu email
                )
            except Exception as e:
                print(f'Erro ao enviar email: {e}')

            messages.success(request, 'Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.')
            return redirect('pro_final:cadastro')
    else:
        form = ContatoForm()

    context = {
        'form': form
    }

    return render(request, 'pro_final/cadastro.html', context)
  

