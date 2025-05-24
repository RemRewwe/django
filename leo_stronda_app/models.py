from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(
        upload_to= '',
        blank=True,
        null=True
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

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
