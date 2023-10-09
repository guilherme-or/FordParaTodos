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


class Personalizacao(models.Model):
    nome = models.CharField(max_length=64)
    descricao = models.TextField()
    preco = models.FloatField()

    class Meta:
        db_table = "personalizacoes"
        verbose_name_plural = "Personalizações"

    def __str__(self):
        return self.nome


class Carro(models.Model):
    modelo = models.CharField(max_length=64)
    descricao = models.CharField(max_length=300, default="")
    ano = models.PositiveIntegerField()  # 1999
    motor = models.CharField(max_length=64)
    potencia = models.CharField(max_length=32)
    transmissao = models.CharField(max_length=32)
    preco = models.FloatField(default=0.0)
    cores = models.ManyToManyField(Cor)
    personalizacoes = models.ManyToManyField(
        Personalizacao, related_name="carro_personalizacoes"
    )

    class Meta:
        db_table = "carros"
        verbose_name_plural = "Carros"

    def __str__(self):
        return self.modelo


class Solicitacao(models.Model):
    STATUS = [(0, "Enviada"), (1, "Em negociação"), (2, "Em produção"), (3, "Atendida")]
    KEY = 12345

    observacao = models.TextField()
    data_criacao = models.DateTimeField("Data de criação", auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    preco = models.FloatField(default=0)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, null=False)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE, null=False)
    personalizacoes = models.ManyToManyField(
        Personalizacao, related_name="solicitacao_personalizacoes"
    )

    class Meta:
        db_table = "solicitacoes"
        verbose_name_plural = "Solicitações"

    def get_status(self):
        return self.STATUS[self.status][1]

    def get_real_id(id, key=KEY):
        return id / key

    def generate_custom_id(self):
        return self.id * self.KEY

    def __str__(self):
        return self.data_criacao.strftime("%d-%m-%Y")
