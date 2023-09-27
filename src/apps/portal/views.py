from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from .models import Carro, Cor


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
    return render(
        request,
        "portal/detalhe.html",
        {
            "carro": carro,
            "personalizacoes": carro.personalizacoes.all(),
            "cores": carro.cores.all(),
        },
    )


@require_http_methods(["GET"])
def checkout(request):
    query_dict = request.GET

    if request.session.get("usuario", None) is None:
        request.session["not_logged_data"] = {
            "cor": query_dict.get("cor", None),
            "personalizacoes": query_dict.getlist("personalizacoes", None),
        }
        request.session["next_page"] = "portal.checkout"
        return redirect("portal.login")

    cor = Cor.objects.get(pk=query_dict.get("cor"))

    return render(request, "portal/checkout.html")

@csrf_exempt
@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "GET":
        return render(request, "portal/login.html")

    if request.method == "POST":
        form = request.POST
        email = form.get('email', None)
        senha = form.get('senha', None)
        print(form, email, senha)
        return render(request, "portal/login.html")

@csrf_exempt
@require_http_methods(["GET", "POST"])
def logout(request):
    request.session.clear()
    request.session.flush()

    if request.method == "GET":
        return redirect('portal.index')
    
    return HttpResponse(status=200)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def criar_conta(request):
    if request.method == "GET":
        return render(request, "portal/criar_conta.html")

    if request.method == "POST":
        return render(request, "portal/criar_conta.html")
