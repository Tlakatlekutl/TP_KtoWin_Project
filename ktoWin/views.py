from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'ktoWin/index.html', {})


def post(request):
    return render(request, 'ktoWin/post.html', {})


def new_post(request):
    return render(request, 'ktoWin/new.html', {})


def settings(request):
    return render(request, 'ktoWin/settings.html', {})


def signup(request):
    return render(request, 'ktoWin/signup.html', {})


def find(request):
    return render(request, 'ktoWin/find.html', {})


def test(request):
    return render(request, 'ktoWin/test.html', {})
