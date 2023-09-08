from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def loginpage(request):
    template="Heloo world!"
    return HttpResponse(template)