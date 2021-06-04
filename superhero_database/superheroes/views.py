from django.shortcuts import render
from .models import SuperHeroes
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    all_superheroes = SuperHeroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def detail(request, superheroes_id):
    detail_page = SuperHeroes.objects.get(pk=superheroes_id)
    context = {
        'superheroes': detail_page
    }
    return render(request, 'superheroes/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = SuperHeroes(name=name, alter_ego=alter_ego, primary_ability=primary_ability,
                                    secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def edit(request, superheroes_id):
    edit_info = SuperHeroes.objects.get(pk=superheroes_id)
    if request.method == 'POST':
        edit_info.name = request.POST.get('name')
        edit_info.alter_ego = request.POST.get('alter_ego')
        edit_info.primary_ability = request.POST.get('primary_ability')
        edit_info.secondary_ability = request.POST.get('secondary_ability')
        edit_info.catchphrase = request.POST.get('catchphrase')
        edit_info.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        context = {
            'superheroes': edit_info
        }
        return render(request, 'superheroes/index.html', context)


# def delete(request, superheroes_id):
#     pass
