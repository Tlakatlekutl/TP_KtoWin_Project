from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Post, Comment, Like
from .forms import PostForm, SignupUserForm, SignupProfileForm, CommentForm, SettingsNickname
from .forms import ChangePasswordForm
from django.contrib.auth.decorators import login_required


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
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post_by_pk
            comment.like_count = 0
            c_id = form.save().id
            return redirect(reverse("post_by_pk", kwargs={"pk": pk}))
    else:
        form = CommentForm()
    return render(request, 'ktoWin/post.html',
                  {'post': post_by_pk, 'comments': comments, 'form': form})


def find_by_tag(request, tag):
    try:
        post_by_tag, tag_name = Post.objects.posts_by_tag(tag)
    except:
        return HttpResponseBadRequest("Very bad request")
    page = request.GET.get('page')
    object_page, paginator = paginate(post_by_tag, page)
    return render(request, 'ktoWin/find_by_tag.html', {'posts': object_page, 'tag': tag_name.name})


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            p_id = form.save().id
            return redirect(reverse("post_by_pk", kwargs={"pk": p_id}))
            # return HttpResponseRedirect('http://ktowin.my/post/'+str(p_id))
    else:
        form = PostForm()
    return render(request, 'ktoWin/new.html', {'form': form})


@login_required
def changePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
    else:
        form = ChangePasswordForm()
    return render(request, 'ktoWin/changePassword.html', {'form': form})


@login_required
def settings(request):
    user = request.user
    if request.method == 'POST':
        u_form = SettingsNickname(request.POST, instance=user)
        p_form = SignupProfileForm(request.POST, request.FILES,  instance=user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect(reverse("settings"))
    else:
        u_form = SettingsNickname(instance=user)
        p_form = SignupProfileForm(instance=user.userprofile)
    return render(request, 'ktoWin/settings.html', {'u_form': u_form,
                                                    'p_form': p_form
                                                    })


# @require_POST
def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({})
    else:
        return JsonResponse({'status': 'error',
                             'message': 'Incorrect password or login'},
                            status=403)


@login_required
def logoutUser(request):
    logout(request)
    return redirect(reverse('index'))


def signup(request):
    if request.method == 'POST':
        u_form = SignupUserForm(request.POST,  prefix="form1")
        p_form = SignupProfileForm(request.POST, request.FILES,  prefix="form2")
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse("index"))
    else:
        u_form = SignupUserForm(prefix="form1")
        p_form = SignupProfileForm(prefix="form2")
    return render(request, 'ktoWin/signup.html', {'u_form': u_form,
                                                  'p_form': p_form
                                                  })


def search(request):
    return render(request, 'ktoWin/find.html', {})


def test(request):
    return render(request, 'ktoWin/test.html', {})


@login_required
def like(request):
    if request.method == 'POST':
        user = request.user
        try:
            id_r = int(request.POST.get('id'))
            ct = request.POST.get('ct')
            vote = request.POST.get('vote')
            if ct == 'post':
                c_type = get_object_or_404(Post, id=id_r)
            elif ct == 'comment':
                c_type = get_object_or_404(Comment, id=id_r)

            if vote == 'like':
                v_int = 1
            elif vote == 'dislike':
                v_int = -1

            count = c_type.like_count + v_int
            l = Like(user=request.user, content_object=c_type, object_id=id_r, like_status=v_int)
            l.save()
            return JsonResponse({'id': id_r, 'count': count})
        except:
            return JsonResponse({'status': 'error', 'msg': 'aaaaa'}, status=500)
    else:
        return JsonResponse({'status': 'error'}, status=500)

        #     temp = Like.objects.get(object_id=id_r, content_type=c_type, user=request.user)
        # except Like.DoesNotExist:
        #     count = c_type.like_count + v_int
        #     l = Like(user=request.user, content_object=c_type, object_id=id_r, like_status=v_int)
        #     l.save()
        #     return JsonResponse({'id': id_r, 'count': count})
        # return JsonResponse({'status': 'error', 'msg': 'aaaaa'}, status=500)
