from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    range_40 = range(1, 41)
    return render(request, 'generator/home.html', {'password': "1234test", 'range_40': range_40})
def about(request):
    return render(request, 'generator/about.html')

def password(request):

    
    print(request.GET)
    characters = ['']
    if request.GET.get('uppercase'):
        characters.extend(list('ACDEFGHIJKLMNOPQRSTUVWZ'))
    if request.GET.get('special'):
        characters.extend(list('*!#?@'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    if request.GET.get('lower'):
        characters.extend(list('abscdefghijklmnopqrstuvwyz'))


    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password': thepassword})

