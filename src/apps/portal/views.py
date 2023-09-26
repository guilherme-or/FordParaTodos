from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404
from .models import Carro


@require_http_methods(["GET"])
def index(request):
    return render(request, "portal/index.html")


@require_http_methods(["GET"])
def catalogo(request):
    return render(
        request,
        "portal/catalogo.html",
        {"carros": Carro.objects.all()},
    )


@require_http_methods(["GET"])
def detalhe(request, id_carro=0):
    carro = get_object_or_404(Carro, pk=id_carro)
    return render(request, "portal/detalhe.html", {"carro": carro})


@require_http_methods(["GET"])
def checkout(request):
    print(request)
    return render(request, "portal/checkout.html")
