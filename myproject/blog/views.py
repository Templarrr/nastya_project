from django.shortcuts import render
from django.http import HttpResponse
import datetime


class MyStruct(object):
    pass


def index(request):
    c = MyStruct()
    c.company = 'Cool Star'
    c.title = 'Cool Star Blog'
    c.author_name = 'Jhon Smith'
    c.pub_date = datetime.datetime.now()
    c.article_list = [{'title':'Title1','text':'text1'},
                      {'title':'Title2','text':'text2'},
                      {'title':'Title3','text':'text3'}]
    return render(request, 'blog/index.html',  c.__dict__)
