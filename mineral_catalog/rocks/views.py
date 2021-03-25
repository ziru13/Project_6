import json

from django.shortcuts import render, redirect

# Create your views here.
# from django.shortcuts import HttpResponse
from .models import Rock


def load_rocks(request):
    json_file = 'assets/minerals.json'  # 要指名文件目录

    # open json
    with open(json_file, encoding='utf-8') as f:
        rocks = json.load(f)

    for rock in rocks:
        # print(rock['name'])
        # create rock object
        Rock.objects.create(
            name=rock['name'])     # 从Rock模型中

    return redirect('rocks:rock_list')


def rock_list(request):
    rocks = Rock.objects.all()
    # output = ', '.join(str(rock) for rock in rocks)
    return render(request, 'rocks/rock_list.html', {'rocks': rocks})
