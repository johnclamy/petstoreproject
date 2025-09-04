from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    posts = Post.published.all()

    template_data['page_title'] = 'Blog posts on Petzy | blog list page'
    template_data['posts'] = posts

    return render(request, 'blog/post/index.html', {'data': template_data})


def post_detail_page(request: HttpRequest, year: int, month: int, day: int, post: str) -> HttpResponse:
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )

    template_data = {}
    template_data['page_title'] = 'Blog post titled "{0}" | blog detail page'.format(post.title)
    template_data['post'] = post 

    return render(request, 'blog/post/detail.html', {'data': template_data})
