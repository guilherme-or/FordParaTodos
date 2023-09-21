from django.shortcuts import render


def index(request):
    return render(request, "portal/index.html")


def catalogo(request):
    carros = [
        {
            "modelo": "Bronco Sport",
            "ano": 2024,
        },
        {
            "modelo": "Ranger",
            "ano": 2024,
        },
    ]

    return render(request, "portal/catalogo.html", {"carros": carros})
