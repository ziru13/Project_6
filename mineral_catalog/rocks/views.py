import json
import random
import string

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Rock

json_file = 'assets/minerals.json'  # 要指名文件目录


def load_rocks(request):
    Rock.objects.all().delete()         # 每次load rocks之前都要将之前的删除，不然会一直累计

    # open json
    with open(json_file, encoding='utf-8') as f:
        rocks = json.load(f)

    for rock in rocks:
        # create rock object
        Rock.objects.create(         # 从Rock模型中创建一个rock
            name=rock['name'] if 'name' in rock else '',
            category=rock['category'] if 'category' in rock else '',
            image_caption=rock['image caption'] if 'image caption' in rock else '',
            formula=rock['formula'] if 'formula' in rock else '',
            strunz_classification=rock['strunz classification'] if 'strunz classification' in rock else '',
            unit_cell=rock['unit cell'] if 'unit cell' in rock else '',
            color=rock['color'] if 'color' in rock else '',
            crystal_system=rock['cry system'] if 'cry system' in rock else '',
            crystal_symmetry=rock['crystal symmetry'] if 'crystal symmetry' in rock else '',
            cleavage=rock['cleavage'] if 'cleavage' in rock else '',
            mohs_scale_hardness=rock['mohs scale hardness'] if 'mohs scale hardness' in rock else '',
            luster=rock['luster'] if 'luster' in rock else '',
            streak=rock['streak'] if 'streak' in rock else '',
            diaphaneity=rock['diaphaneity'] if 'diaphaneity' in rock else '',
            optical_properties=rock['optical properties'] if 'optical properties' in rock else '',
            refractive_index=rock['refractive index'] if 'refractive index' in rock else '',
            crystal_habit=rock['crystal habit'] if 'crystal habit' in rock else '',
            specific_gravity=rock['specific gravity'] if 'specific gravity' in rock else ''
        )
    return redirect('rocks:rock_list')


def rock_list(request):
    rocks = Rock.objects.all()
    return render(request, 'rocks/rock_list.html', {'rocks': rocks})


def rock_detail(request, pk):
    rock = get_object_or_404(Rock, pk=pk)
    return render(request, 'rocks/rock_detail.html', {'rock': rock})


def random_rock(request):
    rocks = list(Rock.objects.all())
    rock = random.choice(rocks)
    return render(request, 'rocks/rock_detail.html', {'rock': rock})


# def sort_rocks(request, letter):
#     letters = list(string.ascii_uppercase)
#     rocks_a = Rock.objects.filter(name__startswith=letter)
#     return render(request, 'rocks/rock_a.html', {'letters': letters,
#                                                  'rocks_a': rocks_a})

def sort_rocks(request, letter):
    rocks_cap = Rock.objects.filter(name__startswith=letter)
    return render(request, 'rocks/rocks_cap.html', {'rocks_cap': rocks_cap})
