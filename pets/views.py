from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


pets = [
    {
        'id': 1,
        'breed': 'Tibetan Mastiff',
        'name': 'Bear',
        'gender': 'M',
        'price': 3999.99,
        'is_kids_friendly': True,
        'short_descr': 'The Tibetan Mastiff is a large Tibetan dog breed. Its double coat is medium to long, subject to climate, and found in a wide variety of colors, including solid black, black and tan, various shades of red and bluish-gray, and sometimes with white markings around its neck, chest and legs.',
        'long_descr': ''
    },
    {
        'id': 2,
        'breed': 'Samoyed',
        'name': 'Charlie',
        'gender': 'F',
        'price': 3699.99,
        'is_kids_friendly': True,
        'short_descr': 'The Samoyed is a breed of herding dog with a thick, white, double-layered coat. They are spitz-type dogs which take their name from the Samoyedic peoples of Siberia. Descending from the Nenets Herding Laika, they are domesticated animals that assist in herding, hunting, protection and sled-pulling.',
        'long_descr': ''
    },
    {
        'id': 3,
        'breed': 'Chow Chow',
        'name': 'Milo',
        'gender': 'M',
        'price': 7999.99,
        'is_kids_friendly': False,
        'short_descr': 'The Chow Chow is a spitz-type of dog breed originally from Northern China. The Chow Chow is a sturdily built dog, square in profile, with a broad skull and small, triangular, erect ears with rounded tips. The breed is known for a very dense double coat that is either smooth or rough.',
        'long_descr': ''
    },
    {
        'id': 4,
        'breed': 'English Bulldog',
        'name': 'Bailey',
        'gender': 'M',
        'price': 4999.99,
        'is_kids_friendly': True,
        'short_descr': 'The Bulldog is a British breed of dog of mastiff type. It may also be known as the English Bulldog or British Bulldog. It is a stocky, muscular dog of medium size, with a large head, thick folds of skin around the face and shoulders and a relatively flat face with a protruding lower jaw.',
        'long_descr': ''
    },
    {
        'id': 5,
        'breed': 'French Bulldog',
        'name': 'Lola',
        'gender': 'F',
        'price': 4499.99,
        'is_kids_friendly': True,
        'short_descr': 'The French Bulldog is a French breed of companion dog or toy dog. It appeared in Paris in the mid-nineteenth century, apparently the result of cross-breeding of Toy Bulldogs imported from England and local Parisian ratters.',
        'long_descr': ''
    },
    {
        'id': 6,
        'breed': 'Bernese Mountain Dog',
        'name': 'Max',
        'gender': 'M',
        'price': 2688,
        'is_kids_friendly': True,
        'short_descr': 'The Bernese Mountain Dog, German: Berner Sennenhund or Dürrbächler, is a large dog breed originating from the canton of Bern, Switzerland and the Swiss Alps. It is one of four Sennenhund-type breeds, with ancestral roots in Roman mastiffs.',
        'long_descr': ''
    },
    {
        'id': 7,
        'breed': 'Dachshund (Miniature)',
        'name': 'Daisy',
        'gender': 'F',
        'price': 1575,
        'is_kids_friendly': False,
        'short_descr': 'Miniature Dachshunds are small, long-bodied hounds with short legs, known for their playful and affectionate nature. They are a smaller version of the standard Dachshund, typically weighing 11 pounds or less. These dogs are known for their loyalty, courage, and tendency to bark, making them good watchdogs.',
        'long_descr': ''
    },
    {
        'id': 8,
        'breed': 'Labrador Retriever',
        'name': 'Bella',
        'gender': 'F',
        'price': 999.99,
        'is_kids_friendly': True,
        'short_descr': '''The Labrador Retriever, also known simply as the Labrador or Lab, is a British breed of retriever gun dog. It was developed in the United Kingdom from St. John's water dogs imported from the colony of Newfoundland, and was named after the Labrador region of that colony.''',
        'long_descr': ''
    },
    {
        'id': 9,
        'breed': 'Jack Russell Terrier',
        'name': 'Smythie',
        'gender': 'M',
        'price': 459.99,
        'is_kids_friendly': False,
        'short_descr': 'The Jack Russell Terrier is a British breed of small terrier. It is principally white-bodied and smooth, rough or broken-coated, and can be any colour.',
        'long_descr': ''
    },
    {
        'id': 10,
        'breed': 'Border Collie',
        'name': 'Rosie',
        'gender': 'F',
        'price': 1399.99,
        'is_kids_friendly': True,
        'short_descr': 'Border Collies can be good family dogs, but they are best suited for active families who can meet their substantial exercise and mental stimulation needs.',
        'long_descr': ''
    },
    {
        'id': 11,
        'breed': 'Cavalier King Charles Spaniel',
        'name': 'Molly',
        'gender': 'F',
        'price': 873,
        'is_kids_friendly': True,
        'short_descr': 'They are known for their gentle, affectionate, and playful nature, making them excellent family pets. They are also adaptable and eager to please, which contributes to their compatibility with kids.',
        'long_descr': ''
    },
    {
        'id': 12,
        'breed': 'Staffordshire Bull Terrier',
        'name': 'Sadie',
        'gender': 'F',
        'price': 965,
        'is_kids_friendly': True,
        'short_descr': 'The Staffordshire Bull Terrier, also called the Staffy or Stafford, is a purebred dog of small to medium size in the terrier group that originated in the northern parts of Birmingham and in the Black Country of Staffordshire, for which it is named.',
        'long_descr': ''
    },
    {
        'id': 13,
        'breed': 'Labradoodle',
        'name': 'Rocky',
        'gender': 'M',
        'price': 1499.99,
        'is_kids_friendly': True,
        'short_descr': 'A labradoodle is a crossbreed dog created by crossing a Labrador Retriever and a Standard or Miniature Poodle. Labradoodles were intended to be a good choice for people allergic to canine dander.',
        'long_descr': ''
    },
]


def pet_list_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    template_data['page_title'] = 'Pups available for sale | Pet list page'
    template_data['pets'] = pets

    return render(request, 'pets/index.html', {'data': template_data})


def pet_detail_page(request: HttpRequest, id: int) -> HttpResponse:
    template_data = {}
    pet = pets[id - 1]

    template_data['page_title'] = "Your pet selection was {0} ({1}) | Detail pet page".format(pet['name'], pet['breed'])
    template_data['pet'] = pet

    return render(request, 'pets/detail.html', {'data': template_data})