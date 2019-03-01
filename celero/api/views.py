from django.http import HttpResponse


def home(request):
    return HttpResponse('Olá, sou uma API!')
