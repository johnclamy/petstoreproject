from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post


def post_list_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    posts = Post.published.all()

    template_data['page_title'] = 'Blog posts on Petzy | blog list page'
    template_data['posts'] = posts

    return render(request, 'blog/post/index.html', {'data': template_data})
