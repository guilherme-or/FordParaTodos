from django.shortcuts import render


def index(request):
    return render(request, 'portal/index.html')
def catalogo(request):
    return render(request, 'portal/catalogo.html')
