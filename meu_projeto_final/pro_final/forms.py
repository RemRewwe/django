from django import forms
from .models import Login, UserProfile, Cadastro

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['nomeusuario', 'senha']  # Campos do formulário

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [] # Apenas o campo de foto


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nomeusuario', 'email', 'senha']

