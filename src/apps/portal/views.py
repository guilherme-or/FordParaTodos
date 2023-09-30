from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Carro, Cor, Personalizacao, Usuario, Solicitacao


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
    if request.session.get("id_usuario", None) is None:
        request.session["not_logged_data"] = {
            "carro": query_dict.get("carro", None),
            "cor": query_dict.get("cor", None),
            "personalizacoes": query_dict.getlist("personalizacoes", None),
        }
        request.session["next_page"] = "portal.checkout"

        return redirect("portal.login")

    request.session["next_page"] = None
    not_logged_data = request.session.get("not_logged_data", {})

    id_usuario = request.session["id_usuario"]
    usuario = None
    try:
        usuario = Usuario.objects.get(pk=id_usuario)
    except Exception:
        return redirect("portal.catalogo")

    id_carro = query_dict.get("carro", not_logged_data.get("carro", None))
    carro = Carro.objects.get(pk=id_carro)

    id_cor = query_dict.get("cor", not_logged_data.get("cor", None))
    cor = Cor.objects.get(pk=id_cor)

    personalizacoes = []
    for id_personalizacao in query_dict.getlist(
        "personalizacoes", not_logged_data.get("personalizacoes", None)
    ):
        personalizacao = Personalizacao.objects.get(pk=id_personalizacao)
        personalizacoes.append(personalizacao)

    return render(
        request,
        "portal/checkout.html",
        {
            "usuario": usuario,
            "carro": carro,
            "cor": cor,
            "personalizacoes": personalizacoes,
            "previous_url": request.META["HTTP_REFERER"],
        },
    )


@csrf_exempt
@require_http_methods(["POST"])
def solicitacao(request):
    form = request.POST
    form_carro = Carro.objects.get(pk=form.get("carro", None))
    form_cor = Cor.objects.get(pk=form.get("cor", None))
    form_observacao = form.get("observacao", "")
    session_usuario = Usuario.objects.get(pk=request.session["id_usuario"])

    nova_solicitacao = None
    try:
        nova_solicitacao = Solicitacao.objects.create(
            observacao=form_observacao,
            usuario=session_usuario,
            carro=form_carro,
            cor=form_cor,
        )
    except Exception:
        redirect("portal.checkout")

    for id_personalizacao in form.getlist("personalizacoes", []):
        personalizacao = Personalizacao.objects.get(pk=id_personalizacao)
        nova_solicitacao.personalizacoes.add(personalizacao)

    nova_solicitacao.save()

    return redirect("portal.agradecimento")


@require_http_methods(["GET"])
def agradecimento(request):
    return render(request, "portal/agradecimento.html")


@csrf_exempt
@require_http_methods(["GET", "POST"])
def login(request):
    if request.session.get("id_usuario", None) is not None:
        return redirect(request.META["HTTP_REFERER"])

    if request.method == "GET":
        return render(
            request,
            "portal/login.html",
            {"previous_url": request.META.get("HTTP_REFERER", reverse("portal.index"))},
        )

    if request.method == "POST":
        form = request.POST
        email = form.get("email", None)
        senha = form.get("senha", None)

        usuario = None
        usuario_not_found = {"error": "Usuário não encontrado ou senha incorreta"}

        try:
            usuario = Usuario.objects.get(email__exact=email)
        except Exception:
            return render(request, "portal/login.html", usuario_not_found)

        if usuario is None or usuario.senha != senha:
            return render(request, "portal/login.html", usuario_not_found)

        request.session["id_usuario"] = usuario.id
        redirect_page = request.session.get("next_page", "portal.index")
        return redirect(redirect_page)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def criar_conta(request):
    if request.method == "GET":
        return render(request, "portal/criar_conta.html")

    if request.method == "POST":
        form = request.POST

        form_nome = form.get("nome")
        form_sobrenome = form.get("sobrenome")
        form_data_nascimento = form.get("data_nascimento")
        form_cep = form.get("cep")
        form_celular = form.get("celular")
        form_email = form.get("email")
        form_senha = form.get("senha")

        novo_usuario = None
        usuario_incompleto = {
            "error": "Não foi possível criar o usuário, \
                cheque os campos e tente novamente"
        }
        try:
            novo_usuario = Usuario.objects.create(
                nome=form_nome,
                sobrenome=form_sobrenome,
                data_nascimento=form_data_nascimento,
                cep=form_cep,
                celular=form_celular,
                email=form_email,
                senha=form_senha,
            )
        except Exception:
            return render(
                request,
                "portal/criar_conta.html",
                usuario_incompleto,
            )

        if novo_usuario is None:
            return render(
                request,
                "portal/criar_conta.html",
                usuario_incompleto,
            )

        request.session["id_usuario"] = novo_usuario.id
        redirect_page = request.session.get("next_page", "portal.index")
        return redirect(redirect_page)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def logout(request):
    request.session.clear()
    request.session.flush()

    return redirect("portal.index")
