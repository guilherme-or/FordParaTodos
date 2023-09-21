from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    admin = models.BooleanField(default=False)
    senha = models.CharField(max_length=128)
    data_nascimento = models.DateField("Data de nascimento")
    email = models.EmailField(max_length=128, unique=True)
    celular = models.CharField(max_length=19, null=True)  # +55 (11) 91234-5678
    cep = models.CharField(max_length=8)  # 12345678

    class Meta:
        db_table = "usuarios"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome


class Cor(models.Model):
    nome = models.CharField(max_length=32)
    codigo = models.CharField(max_length=9)  # #RRGGBB00

    class Meta:
        db_table = "cores"
        verbose_name_plural = "Cores"

    def __str__(self):
        return self.nome


class Carro(models.Model):
    modelo = models.CharField(max_length=64)
    ano = models.PositiveIntegerField()  # 1999
    cores = models.ManyToManyField(Cor)
    
    class Meta:
        db_table = "carros"
        verbose_name_plural = "Carros"

    def __str__(self):
        return self.modelo


class Personalizacao(models.Model):
    nome = models.CharField(max_length=64)
    descricao = models.TextField()
    carros = models.ManyToManyField(Carro, related_name="carros")

    class Meta:
        db_table = "personalizacoes"
        verbose_name_plural = "Personalizações"

    def __str__(self):
        return self.nome


class Solicitacao(models.Model):
    descricao = models.TextField()
    data_criacao = models.DateTimeField("Data de criação", auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    personalizacoes = models.ManyToManyField(
        Personalizacao, related_name="personalizacoes"
    )

    class Meta:
        db_table = "solicitacoes"
        verbose_name_plural = "Solicitações"

    def __str__(self):
        return self.data_criacao
