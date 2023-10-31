
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request, "home.html",{})

def contact_view(request,*args, **kwargs):
    return render(request,"contact.html")

def about_view(request,*args, **kwargs):
    my_context = {
        'my_text' : 'This is about using context in template.',
        'my_number' : 1234,
        'my_address' : 'asdfghjkl'
    }
    return render(request,"about.html", my_context)

def social_view(request,*args, **kwargs):
    return render("<h1>social page</h1>")