from django.shortcuts import HttpResponse, render


def hello_world(request):
    return render(request, 'home.html')