from django.http import HttpResponse


def index(request):
    return HttpResponse("Bracketology welcomes you!")
