from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(User):
    grupo = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'