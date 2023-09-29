from apps.portal.models import Usuario, Cor, Carro, Personalizacao, Solicitacao

# Limpar os dados

Usuario.objects.all().delete()
Cor.objects.all().delete()
Carro.objects.all().delete()
Personalizacao.objects.all().delete()
Solicitacao.objects.all().delete()

# Usuario(ID, "Nome", "Sobrenome", admin, "senha", data_nascimento, "email", "celular", "cep")

u1 = Usuario(
    1,
    "Guilherme",
    "de Oliveira Rocha",
    True,
    "admin",
    "2002-08-15",
    "guilherme@email.com",
    "(11) 97070-7070",
    "70707-070",
)
u1.save()

u2 = Usuario(
    2,
    "Gabriel",
    "Hiroaki Nakasone",
    True,
    "admin",
    "2000-03-01",
    "hiro@email.com",
    "(11) 91234-5678",
    "12345-678",
)
u2.save()

u3 = Usuario(
    3,
    "Eduardo",
    "de Oliveira",
    False,
    "usuario",
    "2003-01-01",
    "edu@email.com",
    "11987654321",
    "98765432",
)
u3.save()

u4 = Usuario(
    4,
    "Jooji",
    "Daniel Sugahara",
    False,
    "usuario",
    "1997-10-14",
    "jooji@email.com",
    "11900000000",
    "00000000",
)
u4.save()


# Cor (ID, "Nome", "Codigo")

co1 = Cor(1, "Branco Ártico", "#e6ebf1")
co1.save()

co2 = Cor(2, "Preto Astúrias", "#0a0a12")
co2.save()

co3 = Cor(3, "Vermelho Aurora", "#ce3a38")
co3.save()

co4 = Cor(4, "Azul Atlas", "#0252b5")
co4.save()

# Personalizacao(ID, "Nome", "Descricao")

p1 = Personalizacao(
    1,
    "Banco de Transferência Manual",
    "O banco de transferência manual auxilia na passagem entre o banco do carro e a \
        cadeira de rodas, facilitando a enterada e saída do condutor ou passageiro",
)
p1.save()

p2 = Personalizacao(
    2,
    "Acelerador e Freio Manual",
    "O Acelerador e Freio Manual é uma adaptação veicular PCD destinado ao uso de \
        motoristas com deficiência ou limitações nos membros superiores",
)
p2.save()

p3 = Personalizacao(
    3,
    "Pomo Giratório",
    "O pomo giratório permite que o motorista gire totalmente o volante em 360° e \
        auxilia na preensão para pessoas com limitações de movimento nas mãos",
)
p3.save()

p4 = Personalizacao(
    4,
    "Central de Comandos",
    "A Central de Comandos de Painel ao Volante é um dispositivo que permite o controle\
        dos comandos elétricos de dirigibilidade(seta, faróis, lavadores, limpadores e \
            buzinas) e do volante do veículo simultaneamente",
)
p4.save()

p5 = Personalizacao(
    5,
    "PPU",
    "O PPU - Prolongamento de Pedais Universal - é um equipamento que aproxima do \
        motorista, o controle de comandos do acelerador, freio de serviço e embreagem",
)
p5.save()


# Carro(ID, "Modelo", "Descricao", Ano, "Motor", "Potência", "Transmissão").save()

ca1 = Carro(
    1,
    "Ford Maverick",
    "Esportiva, versátil, conectada e com a robustez da família Raça Forte. \
    Equipada com motor 2.0L EcoBoost® (253 cv / 380 Nm) e transmissão automática \
    de 8 velocidades, a Nova Ford Maverick entrega uma performance surpreendente, \
    trazendo esportividade e versatilidade para todos os momentos.",
    2023,
    "2.0L EcoBoost",
    "253CV @ 5500 rpm",
    "Automática 8 Velocidades",
)
ca1.save()

ca1.personalizacoes.add(p1)
ca1.personalizacoes.add(p2)
ca1.personalizacoes.add(p3)
ca1.personalizacoes.add(p4)
ca1.personalizacoes.add(p5)

ca1.cores.add(co1)
ca1.cores.add(co2)
ca1.cores.add(co3)
ca1.cores.add(co4)

ca1.save()

ca2 = Carro(
    2,
    "Ford Bronco Sport",
    "Ford Bronco Sport, um SUV imbatível. Performance e capacidade off-road \
    excepcionais, tecnologia, conectividade e segurança para superar todo \
    tipo de desafio: dentro e fora de estrada.",
    2023,
    "2.0L Turbo EcoBoost GTDi",
    "253CV @ 5500 rpm",
    "Automática 8 Velocidades",
)
ca2.save()

ca2.personalizacoes.add(p1)
ca2.personalizacoes.add(p3)
ca2.personalizacoes.add(p5)

ca2.cores.add(co1)
ca2.cores.add(co2)

ca2.save()

ca3 = Carro(
    3,
    "Ford Territory",
    "Um novo conceito de design, conforto, tecnologia e segurança. Ele chega com \
    um design totalmente novo, mais espaço interno e conforto para todos os passageiros, \
    mais potência, com avançados recursos de tecnologia semiautônomos e segurança.",
    2024,
    "1.5L EcoBoost",
    "169CV @ 5500 rpm",
    "Automática de 7 velocidades",
)
ca3.save()

ca3.personalizacoes.add(p2)
ca3.personalizacoes.add(p4)

ca3.cores.add(co3)
ca3.cores.add(co4)

ca3.save()

# Solicitacao(descricao="Descricao",usuario=#)
