from django.db import models


class Usuario(models.Model):
    db_table = "usuarios"
    id_usuario = models.IntegerField(primary_key=True, autoincrement=True)
    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    admin = models.BooleanField(default=False)
    senha = models.CharField(max_length=128)
    data_nascimento = models.DateField("Data de nascimento")
    email = models.EmailField(max_length=128, unique=True)
    celular = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
