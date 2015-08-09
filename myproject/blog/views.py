from django.shortcuts import render
from django.http import HttpResponse
import datetime
from blog.models import Category
from django.views.generic import TemplateView


class MyStruct(object):
    pass

def index(request):
    c = MyStruct()
    c.company = 'Catville'
    c.title = 'Hail the Cat'
    c.author_name = 'Mr Catinsky'
    c.pub_date = datetime.datetime.now()
    c.article_list = [{'title':'Title1','text':'text1'},
                      {'title':'Title2','text':'text2'},
                      {'title':'Title3','text':'text3'}]
    return render(request, 'blog/index.html',  c.__dict__)

class AboutView(TemplateView):
    template_name = "about.html"

def categories(request):
    category_list = Category.objects.order_by('name')
    context_dict = {'category_list':category_list }
    return render(request, 'blog/categories.html', context_dict)

