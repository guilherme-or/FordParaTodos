from apps.portal.models import Cor, Carro, Personalizacao, Solicitacao, Usuario

# Usuario(ID, "Nome", "Sobrenome", admin, "senha", data_nascimento, "email", "celular", "cep")

Usuario(
    1,
    "Guilherme",
    "de Oliveira Rocha",
    True,
    "admin",
    "2002-08-15",
    "emaildoguilherme@email.com",
    "11970707070",
    "70707070",
).save()
Usuario(
    2,
    "Gabriel",
    "Hiroaki Nakasone",
    True,
    "admin",
    "2000-03-01",
    "hiro@email.com",
    "11912345678",
    "12345678",
).save()
Usuario(
    3,
    "Eduardo",
    "de Oliveira",
    False,
    "usuario",
    "2003-01-01",
    "edu@email.com",
    "11987654321",
    "98765432",
).save()
Usuario(
    4,
    "Jooji",
    "Daniel Sugahara",
    False,
    "usuario",
    "1997-10-14",
    "jooji@email.com",
    "11900000000",
    "00000000",
).save()

# Cor (ID, "Nome", "Codigo")

Cor(1, "Branco Ártico", "#e6ebf1").save()
Cor(2, "Preto Astúrias", "#0a0a12").save()
Cor(3, "Vermelho Aurora", "#ce3a38").save()
Cor(4, "Azul Atlas", "#0252b5").save()

# Carro(ID, "Modelo", Ano).save()

Carro(1, "Ford Ranger", 2023).save()
Carro(2, "Ford Bronco Sport", 2023).save()
Carro(3, "Ford Territory", 2022).save()

# Personalizacao(ID, "Nome", "Descricao")

Personalizacao(
    1,
    "Banco de Transferência Manual",
    "O banco de transferência manual auxilia na passagem entre o banco do carro e a \
        cadeira de rodas, facilitando a enterada e saída do condutor ou passageiro",
).save()
Personalizacao(
    2,
    "Acelerador e Freio Manual",
    "O Acelerador e Freio Manual é uma adaptação veicular PCD destinado ao uso de \
        motoristas com deficiência ou limitações nos membros superiores",
).save()
Personalizacao(
    3,
    "Pomo Giratório",
    "O pomo giratório permite que o motorista gire totalmente o volante em 360° e \
        auxilia na preensão para pessoas com limitações de movimento nas mãos",
).save()
Personalizacao(
    4,
    "Central de Comandos",
    "A Central de Comandos de Painel ao Volante é um dispositivo que permite o controle\
        dos comandos elétricos de dirigibilidade(seta, faróis, lavadores, limpadores e \
            buzinas) e do volante do veículo simultaneamente",
).save()
Personalizacao(
    5,
    "PPU",
    "O PPU - Prolongamento de Pedais Universal - é um equipamento que aproxima do \
        motorista, o controle de comandos do acelerador, freio de serviço e embreagem",
).save()

# Solicitacao(descricao="Descricao",usuario=#)

Solicitacao(descricao="Descrição teste solicitação 1", usuario=1).save()
Solicitacao(descricao="Descrição teste solicitação 2", usuario=2).save()

# Solicitacao.objects.all()
