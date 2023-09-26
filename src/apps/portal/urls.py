from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="portal.index"),
    path("catalogo/", views.catalogo, name="portal.catalogo"),
    path("detalhe/<int:id_carro>", views.detalhe, name="portal.detalhe"),
    path("checkout", views.detalhe, name="portal.checkout"),
]
