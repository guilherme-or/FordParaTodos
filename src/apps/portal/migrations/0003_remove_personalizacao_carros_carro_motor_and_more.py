# Generated by Django 4.2.4 on 2023-09-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_solicitacao_data_criacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalizacao',
            name='carros',
        ),
        migrations.AddField(
            model_name='carro',
            name='motor',
            field=models.CharField(default='2.0L EcoBOOST', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carro',
            name='personalizacoes',
            field=models.ManyToManyField(related_name='carro_personalizacoes', to='portal.personalizacao'),
        ),
        migrations.AddField(
            model_name='carro',
            name='potencia',
            field=models.CharField(default='250vc @ 3.250rpm', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carro',
            name='transmissao',
            field=models.CharField(default='Autómatica', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='personalizacoes',
            field=models.ManyToManyField(related_name='solicitacao_personalizacoes', to='portal.personalizacao'),
        ),
    ]
