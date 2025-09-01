from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    posts = Post.published.all()

    template_data['page_title'] = 'Blog posts on Petzy | blog list page'
    template_data['posts'] = posts

    return render(request, 'blog/post/index.html', {'data': template_data})


def post_detail_page(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

    template_data = {}
    template_data['page_title'] = 'Blog post titled "{0}" | blog detail page'.format(post.title)
    template_data['post'] = post 

    return render(request, 'blog/post/post-detail.html', {'data': template_data})
