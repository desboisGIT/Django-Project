from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('hello word')

def item(request):
    return HttpResponse("this is the item views")