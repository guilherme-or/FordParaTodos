from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="portal.index"),
    path("catalogo/", views.catalogo, name="portal.catalogo"),
]
