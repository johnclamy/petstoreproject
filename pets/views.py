from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Pet


def pet_list_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    search_term = request.GET.get('search')
    template_data['page_title'] = 'Pups available for sale | Pet list page'

    if not search_term:
        template_data['pets'] = Pet.objects.all()
    else:
        template_data['pets'] = Pet.objects.filter(breed__icontains=search_term)          

    return render(request, 'pets/index.html', {'data': template_data})


def pet_detail_page(request: HttpRequest, id: int) -> HttpResponse:
    template_data = {}
    pet = Pet.objects.get(id=id)

    template_data['page_title'] = "Your pet selection was {0} ({1}) | Detail pet page".format(pet.name, pet.breed)
    template_data['pet'] = pet

    return render(request, 'pets/detail.html', {'data': template_data})