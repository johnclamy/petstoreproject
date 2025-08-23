from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pet, Review


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
    reviews = Review.objects.filter(pet=pet)

    template_data['page_title'] = "Your pet selection was {0} ({1}) | Detail pet page".format(pet.name, pet.breed)
    template_data['pet'] = pet
    template_data['reviews'] = reviews

    return render(request, 'pets/detail.html', {'data': template_data})


@login_required
def create_review(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == 'POST' and request.POST['comments']:    
        pet = Pet.objects.get(id=id)
        review = Review()

        review.comments = request.POST['comments']
        review.pet = pet
        review.user = request.user
        review.save()

        return redirect('pets.pet_detail_page', id=id)
    else:
        return redirect('pets.pet_detail_page', id=id)


@login_required
def edit_review(request: HttpRequest, id: int, review_id: int) -> HttpResponse:
    review = get_object_or_404(Review, id=review_id)

    if request.user != review.user:
        return redirect('pets.pet_detail_page', id=id)

    if request.method =='GET':
        template_data = {}
        pet = get_object_or_404(Pet, id=id)

        template_data['page_title'] = "Edit review for {0} ({1}) | Edit review page".format(pet.name, pet.breed)
        template_data['review'] = review

        return render(request, 'pets/edit_review.html', {'data': template_data})
    
    elif request.method == 'POST' and request.POST['comments'] != '':
        review.comments = request.POST['comments']
        review.save()

        return redirect('pets.pet_detail_page', id=id)
    else:
        return redirect('pets.pet_detail_page', id=id)