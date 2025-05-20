from django.db import models
from django.contrib.auth.models import user

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(
        upload_to= 'produtos/',
        blank=True,
        null=True
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

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
        upload_to='profile_pics/',
        default='profile_pics/default.png'
    )
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
