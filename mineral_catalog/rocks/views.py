from django.shortcuts import render

# Create your views here.
# from django.shortcuts import HttpResponse
from .models import Rock


def rock_list(request):
    rocks = Rock.objects.all()
    # output = ', '.join(str(rock) for rock in rocks)
    return render(request, 'rocks/rock_list.html', {'rocks': rocks})
