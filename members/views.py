# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Member

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')

    context = {
        'mymembers':mymembers
    }

    return HttpResponse(template.render(context,request))

def greetings (request):
    template = loader.get_template('template_tags.html')
    context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))

  
def fruits(request):
   template = loader.get_template('for_loop.html')
   context = {
    'fruits': ['Apple', 'Banana', 'Orange', 'Kiwi']
     }
   return HttpResponse(template.render(context,request))
   
def forloop(request):
    template = loader.get_template('cars.html')
    context = {
        'cars' : [
            {
                'make': 'Ford',
                'color':'Red',
                'year': 2000
            },
             {
                'make': 'Toyota',
                'colour':'Black',
                'year': 2001
            },
             {
                'make': 'Nissan',
                'colour':'White',
                'year': 2001
            },
             {
                'make': 'Mazda',
                'colour':'Blue',
                'year': 2015
            },
             {
                'make': 'Isuzu',
                'colour':'Maroon',
                'year': 2020
            }
        ]
    }

    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember':mymember
    }

    return HttpResponse(template.render(context,request))