from django.db import models
from django.contrib.auth.models import User

class Login(models.Model):
    nomeusuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=16)
    def __str__(self):
        return self.nomeusuario

class UserProfile(models.Model):
    '''
    Estende o modelo User padrão para:
    - Adicionar foto de perfil
    - Campos personalizados
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(
        upload_to='media/',
        default='blank'
    )
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Cadastro(models.Model):
    nomeusuario = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=16)

    def __str__(self):
        return self.nomeusuario
