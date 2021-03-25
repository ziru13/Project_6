import json

from django.shortcuts import render

# Create your views here.
# from django.shortcuts import HttpResponse
from .models import Rock


def load_rocks(request):
    json_file = 'minerals.json'
    db_file = 'minerals.db'

    # open json
    with open(json_file, encoding='utf-8') as f:
        rocks = json.load(f)

    for rock in rocks:
        print(rock['name'])


def rock_list(request):
    rocks = Rock.objects.all()
    # output = ', '.join(str(rock) for rock in rocks)
    return render(request, 'rocks/rock_list.html', {'rocks': rocks})
