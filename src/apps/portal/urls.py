from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="portal.index"),
    path("catalogo", views.catalogo, name="portal.catalogo"),
    path("detalhe/<int:id_carro>", views.detalhe, name="portal.detalhe"),
    path("checkout", views.checkout, name="portal.checkout"),
    path("solicitacao", views.solicitacao, name="portal.solicitacao"),
    path("agradecimento", views.agradecimento, name="portal.agradecimento"),
    path("login", views.login, name="portal.login"),
    path("criar_conta", views.criar_conta, name="portal.criar_conta"),
    path("logout", views.logout, name="portal.logout"),
]
