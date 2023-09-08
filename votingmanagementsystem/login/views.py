from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def loginpage(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())