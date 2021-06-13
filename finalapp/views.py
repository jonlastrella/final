from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import requests
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')
        password = request.POST['password']
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            firstName=request.POST['firstName'], lastName=request.POST['lastName'], email=request.POST['email'], password=hashed)
    return redirect('/')


def signin(request):
    if request.method == "POST":
        if not User.objects.authenticate(request.POST['email'], request.POST['password']):
            messages.error(request, 'Invalid email and/or password')
            return redirect('/')
        user = User.objects.get(email=request.POST['email'])
        request.session['userId'] = user.id
        request.session['firstName'] = user.firstName.capitalize()
        request.session['lastName'] = user.lastName.capitalize()
        return redirect('/dashboard')
    return redirect('/')


def signout(request):
    request.session.flush()
    return redirect('/')


newsApi = 'https://newsapi.org/v2/top-headlines?country=us&pageSize=5&apiKey=226403d167a7460baad85987d3e7a3aa'
newsApiFull = 'https://newsapi.org/v2/top-headlines?country=us&pageSize=100&apiKey=226403d167a7460baad85987d3e7a3aa'


def dashboard(request):
    if 'userId' not in request.session:
        return render(request, 'unknown.html')
    r = requests.get(newsApiFull)
    r = r.json()
    user = request.session['userId']
    if request.method == 'POST':
        country = request.POST['countries']
        r = requests.get('https://newsapi.org/v2/top-headlines?country=' +
                         country+'&pageSize=100&apiKey=226403d167a7460baad85987d3e7a3aa')
        r = r.json()
    try:
        ProfilePicture.objects.get(user=user)
        context = {
            'users': User.objects.all(),
            'user': User.objects.get(id=user),
            'posts': Post.objects.all(),
            'news': r['articles'],
            'pictures': ProfilePicture.objects.get(user=user)
        }
    except ProfilePicture.DoesNotExist:
        context = {
            'users': User.objects.all(),
            'user': User.objects.get(id=user),
            'posts': Post.objects.all(),
            'news': r['articles'],
        }
    return render(request, 'dashboard.html', context)


def profile(request, userid):
    if 'userId' not in request.session:
        return redirect('/dashboard')
    user = request.session['userId']
    try:
        ProfilePicture.objects.get(user=user)
        context = {
            'user': User.objects.get(id=userid),
            'message': About.objects.all(),
            'post': Post.objects.filter(user=userid),
            'pictures': ProfilePicture.objects.get(user=userid),
        }
    except ProfilePicture.DoesNotExist:
        context = {
            'user': User.objects.get(id=userid),
            'message': About.objects.all(),
            'post': Post.objects.filter(user=userid),
        }
    return render(request, 'profile.html', context)


def edit(request, userid):
    if 'userId' not in request.session:
        return redirect('/dashboard')
    if request.session['userId'] != userid:
        return redirect('/dashboard')
    try:
        context = {
            'user': User.objects.get(id=userid),
            'userInfo': About.objects.all(),
            'pictures': ProfilePicture.objects.get(user=User.objects.get(id=request.session['userId'])),
        }
    except ProfilePicture.DoesNotExist:
        context = {
            'user': User.objects.get(id=userid),
            'userInfo': About.objects.all(),
            'pictures': ProfilePicture.objects.filter(user=User.objects.get(id=request.session['userId']))
        }
    return render(request, 'edit.html', context)


def aboutMe(request):
    user = request.session['userId']
    try:
        delete = About.objects.get(user=user)
        delete.delete()
    except About.DoesNotExist:
        delete = None
    # if About.objects.get(user=user).exists():
    #     delete = About.objects.get(user=user)
    #     delete.delete()
    request.session['aboutMe'] = request.POST['aboutMe']
    request.session['mood'] = request.POST['mood']
    request.session['meet'] = request.POST['meet']
    request.session['motto'] = request.POST['motto']
    text = request.POST['aboutMe']
    user = User.objects.get(id=request.session['userId'])
    mood = request.POST['mood']
    meet = request.POST['meet']
    motto = request.POST['motto']
    About.objects.create(message=text, user=user,
                         mood=mood, meet=meet, motto=motto)
    return redirect('/dashboard')


def profilePicture(request):
    print(ProfilePicture.objects.last().user)
    print(request.session['userId'])
    user = User.objects.get(id=request.session['userId'])
    ProfilePicture(request.FILES['image'],
                   user=user).delete()
    new_file = ProfilePicture(request.FILES['image'], user=user)
    new_file.save()
    return redirect('/dashboard')


def postToProfile(request):
    Post.objects.create(
        user=User.objects.get(id=request.session['userId']), post=request.POST['post'])
    return redirect('/dashboard')


def news(request):
    r = requests.get(newsApiFull)
    r = r.json()
    if request.method == 'POST':
        country = request.POST['countries']
        r = requests.get('https://newsapi.org/v2/top-headlines?country=' +
                         country+'&pageSize=100&apiKey=226403d167a7460baad85987d3e7a3aa')
        r = r.json()
    context = {
        'news': r['articles'],
    }
    return render(request, 'news.html', context)
# def block(request):
#     if request.method == "POST":
#         print(request.POST['blockedUser'])
#         context = {
#             'users': User.objects.all(),
#             # 'abouts': About.objects.all(),
#             'posts': Post.objects.exclude(user=request.POST['blockedUser']),
#             'news': r['articles'],
#         }
#     return redirect('/dashboard')
# 3
# def aboutMe(request):
#     text = request.POST['aboutMe']
#     user = User.objects.get(id=request.session['userId'])
#     mood = request.POST['mood']
#     About.objects.create(message=text, user=user, mood=mood)
#     return redirect('/dashboard')
