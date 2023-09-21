from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404
from .models import Carro


@require_http_methods(["GET"])
def index(request):
    return render(request, "portal/index.html")


@require_http_methods(["GET"])
def catalogo(request):
    motores = [
        "3.0 V6 Diesel 4WD AT",
        "2.0L EcoBOOST",
        "1.5L EcoBoost",
    ]
    
    return render(
        request,
        "portal/catalogo.html",
        {"carros": Carro.objects.all(), "motores": motores},
    )


@require_http_methods(["GET"])
def detalhe(request, id_carro=0):
    carro = get_object_or_404(Carro, pk=id_carro)
    return render(request, "portal/detalhe.html", {"carro": carro})
