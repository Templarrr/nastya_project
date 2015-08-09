# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import datetime 
from blog.models import Category, Post
from django.views.generic import TemplateView

# Create your views here.
#  home_page = None
class MyStruct(object): 
	pass 

def home_page(request):
    return HttpResponse('<html><title>Blog lists</title>Hello Blog <br> "You must be joking!" I can hear you say.</html>')

def index(request):
	posts_list = Post.objects.order_by('title')
	
	category_list = Category.objects.order_by('name')
	context_dict = {'categories_list':category_list, 'posts_list':posts_list }
	return render(request, 'blog/index.html',  context_dict)

def view(request, postslug):
    post = Post.objects.get(slug=postslug)

    context = {'post': post}
    return render_to_response('blog/singlepost.html', context)


class AboutView(TemplateView):
    template_name = "about.html"

def categories(request):
	category_list = Category.objects.order_by('name')
			
	context_dict = {'category_list':category_list }
	return render(request, 'blog/cat.html', context_dict)

def category(request, categoryslug):
	name = Category.objects.get(slug=categoryslug)
	posts = Post.objects.filter(category=name)
	context = {'posts': posts}
	return render(request, 'blog/singlecategory.html', context)