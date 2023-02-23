from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import Person

# Create your views here.


def demo(request):
    obj = Place.objects.all()
    obj1 = Person.objects.all()
    my_dict = {'result': obj, 'result1': obj1}
    return render(request, "index.html", context=my_dict)

def home(request):
    return HttpResponse('<h1 style="background-color:#9fe0b1;">Welcome,This Is Home Page..!!</h1>')


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def details(request):
    return HttpResponse('<div style="color:#223478;padding:20px;background-color:#c2c1a5">Enter Contact Details</div>')


def thanks(request):
    return HttpResponse('<h1 style="background-color:#bf1f3f;color:#f7f7f2">Thanks For The Visit..</h1>')


#def math_op(request):
    #x = int(request.GET['num1'])
    #y = int(request.GET['num2'])
    #add = x+y
    #sub = x-y
    #mul = x*y
    #div = x/y
   # return render(request, "result.html", {'addition': add, 'subtraction': sub, 'multiplication': mul, 'division': div})
