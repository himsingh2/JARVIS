from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("This is my first url i.e blog")

def specific(request):
    list1=[1,2,3,5,'   ','a','m','!']
    return HttpResponse(list1)
    
def article(request,article_id):
    return HttpResponse(article_id)