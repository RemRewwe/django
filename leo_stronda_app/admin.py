from django.contrib import admin
from .models import Produto
from .models import UserProfile

admin.site.register(Produto)
admin.site.register(UserProfile)
