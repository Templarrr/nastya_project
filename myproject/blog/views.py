# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from blog.models import Category, Post
from django.views.generic import TemplateView
from blog.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
#  home_page = None
class MyStruct(object):
    pass


def home_page(request):
    return HttpResponse(
        '<html><title>Blog lists</title>Hello Blog <br> "You must be joking!" I can hear you say.</html>')


def index(request):
    posts_list = Post.objects.order_by('title')

    category_list = Category.objects.order_by('name')
    context_dict = {'categories_list': category_list, 'posts_list': posts_list}
    return render(request, 'blog/index.html', context_dict)


def view(request, postslug):
    post = Post.objects.get(slug=postslug)
    context = {'post': post}
    return render_to_response('blog/singlepost.html', context)


class AboutView(TemplateView):
    template_name = "about.html"


def categories(request):
    category_list = Category.objects.order_by('name')

    context_dict = {'category_list': category_list}
    return render(request, 'blog/cat.html', context_dict)


def category(request, categoryslug):
    name = Category.objects.get(slug=categoryslug)
    posts = Post.objects.filter(category=name)
    context = {'posts': posts}
    return render(request, 'blog/singlecategory.html', context)


def register(request):
    # boolean value
    # Установлено в False при инициализации.
    # Изменим на True при успешной регистрации.

    registered = False

    # Если HTTP POST, обработаем форму.
    if request.method == 'POST':
        # Получаем информацию из форм.
        # Мы используем две формы UserForm и UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # Если обе формы прошли проверку...
        if user_form.is_valid() and profile_form.is_valid():
            # Сохраним данные пользователя из формы в database.
            user = user_form.save()

            # Хешируем пароль с помощью set_password method.

            user.set_password(user.password)
            user.save()
            # Пока пользователь настраивает свой профиль не выполнять commit=False.

            profile = profile_form.save(commit=False)
            profile.user = user
            # Юзер хочет картинку?
            # Если да, предоставим ему поле для ввода картинки.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Сохранить экземпляр модели UserProfile.
            profile.save()

            # Изменить переменную при успешной регистрации.
            registered = True
        else:
            print user_form.errors, profile_form.errors
            # Не HTTP POST, строим два экземпляра ModelForm .
    # Эти формы пустые , предназначены для пользовательских вводов.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    # Render the template depending on the context.
    return render(request, 'blog/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    # If the request is a HTTP POST
    if request.method == 'POST':

        # Эта информация получена из login form.
        # Мы используем request.POST.get('<variable>') вместо  request.POST['<variable>'],
        # потому что request.POST.get('<variable>') вернет None, если значение не существует,
        # в то время ка request.POST['<variable>'] вернет key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Проверка username/password
        user = authenticate(username=username, password=password)
        # Если создан объект user
        # с необходимыми правами -  credentials
        if user:
            # Если account active? Он может быть disabled.
            if user.is_active:
                # Если account правильный и активный, можно логиниться.
                # Переадресуем пользователя на страницу blog.
                login(request, user)
                return HttpResponseRedirect('/blog/')
            else:
                # Используется неактивный account - no logging in!
                return HttpResponse("Your Blog account is disabled.")
    # Запрос не HTTP POST, поэтому показываем login form.
    else:
        # Не переданы variables в template system
        # пустой dictionary object...
        return render(request, 'blog/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

