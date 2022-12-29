from django.shortcuts import render
from django.shortcuts import HttpResponse
import random
# Create your views here.

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    character = list('abcdefghIjklmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    #MAYUS DFHUFEHW
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHJIKLMNIOPQRSTUVWXYZ'))

    #SPECIAL $%(
    if request.GET.get('special'):
        character.extend(list('°!"#$%&/()=?¿}[{]+-*].,-_<>'))

    #NUMBERS 164
    if request.GET.get('numbers'):
        character.extend(list('1234567890'))

    for x in range(length):
        generated_password += random.choice(character)

    return render(request, 'generator/password.html', {'password': generated_password})