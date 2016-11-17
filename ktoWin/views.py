from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from django.contrib.auth.models import User


# Create your views here.

def paginate(objects_list, page):
    # page = request.GET.get('page', 1)

    paginator = Paginator(objects_list, 10)
    try:
        object_page = paginator.page(page)
    except PageNotAnInteger:
        object_page = paginator.page(1)
    except EmptyPage:
        object_page = paginator.page(paginator.num_pages)
    return object_page, paginator


def index(request):
    # new = sorted(posts, reverse=True, key=lambda k: k['date'])
    new = Post.objects.new_posts()
    page = request.GET.get('page')
    object_page, paginator = paginate(new, page)
    return render(request, 'ktoWin/index.html', {'posts': object_page})


def hot(request):
    hot = Post.objects.hot_posts()
    page = request.GET.get('page')
    object_page, paginator = paginate(hot, page)
    return render(request, 'ktoWin/hot.html', {'posts': object_page})


def post(request, pk):
    post_by_pk = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post_by_pk)
    return render(request, 'ktoWin/post.html',
                  {'post': post_by_pk, 'comments': comments})


def find_by_tag(request, tag):
    try:
        post_by_tag, tag_name = Post.objects.posts_by_tag(tag)
    except:
        return HttpResponseBadRequest("Very bad request")
    page = request.GET.get('page')
    object_page, paginator = paginate(post_by_tag, page)
    return render(request, 'ktoWin/find_by_tag.html', {'posts': object_page, 'tag': tag_name.name})


def new_post(request):
    return render(request, 'ktoWin/new.html', {})


def settings(request):
    return render(request, 'ktoWin/settings.html', {})


def signup(request):
    return render(request, 'ktoWin/signup.html', {})


def search(request):
    return render(request, 'ktoWin/find.html', {})


def test(request):
    return render(request, 'ktoWin/test.html', {})
