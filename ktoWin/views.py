from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

# Create your views here.
posts = []
for i in range(0, 30):
    posts.append({
        'id': i,
        'title': 'title ' + str(i),
        'rating': random.randint(1, 1000),
        'date': str(i).zfill(2) + '.11.2016',
        'text': """
                Давно выяснено, что при оценке дизайна и композиции читаемый
                текст мешает сосредоточиться. Lorem Ipsum используют потому,
                что тот обеспечивает более или менее стандартное заполнение шаблона
                """*6,
        'tags': random.sample(['tag1', 'tag2', 'tag3', 'tag4'], random.randint(1, 4)),
        'game': random.choice(['football', 'dota2', 'racing', 'Lol', 'baseball']),
        'post_type': random.choice(['bg-success', 'bg-info', 'bg-warning', '']),
        'comments_count': random.randint(10, 100),
        'comments': [
            {
                'user': 'User1',
                'text': """
                        Давно выяснено, что при оценке дизайна и композиции читаемый
                        текст мешает сосредоточиться. Lorem Ipsum используют потому,
                        что тот обеспечивает более или менее стандартное заполнение шаблона
                        """*4,
                'likes': random.randint(1, 500)
            },
            {
                'user': 'User2',
                'text': """
                        Давно выяснено, что при оценке дизайна и композиции читаемый
                        текст мешает сосредоточиться. Lorem Ipsum используют потому,
                        что тот обеспечивает более или менее стандартное заполнение шаблона
                        """*4,
                'likes': random.randint(1, 500),
            }
        ]
    })


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


def index(request, page=1):
    new = sorted(posts, reverse=True, key=lambda k: k['date'])
    object_page, paginator = paginate(new, page)
    return render(request, 'ktoWin/index.html', {'posts': object_page})


def hot(request, page=1):
    hot = sorted(posts, reverse=True, key=lambda k: k['rating'])
    object_page, paginator = paginate(hot, page)
    return render(request, 'ktoWin/hot.html', {'posts': object_page})


def post(request, pk):
    # post_by_pk = get_object_or_404(model, id=pk)
    try:
        id = int(pk)
        post_by_pk = posts[id]
    except:
        return HttpResponseBadRequest("Very bad request")
    return render(request, 'ktoWin/post.html', {'post': post_by_pk})


def find_by_tag(request, tag, page=1):
    try:
        post_by_tag = [p for p in posts if tag in p['tags']]
    except:
        return HttpResponseBadRequest("Very bad request")

    object_page, paginator = paginate(post_by_tag, page)
    return render(request, 'ktoWin/find_by_tag.html', {'posts': object_page, 'tag': tag})


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
