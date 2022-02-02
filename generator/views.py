from django.shortcuts import render
import random

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    
    chars = list('abcdefghijklmnopqrstvxyz')
    generated_password = ''

    len = request.GET.get('lenght')
    upper = request.GET.get('uppercase')
    special = request.GET.get('special')
    numbers = request.GET.get('numbers')

    if upper:
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTVXYZ'))
    
    if special:
        chars.extend(list('!@#~&()$%¡'))

    if numbers:
        chars.extend(list('0123456789'))

    if (int(len)) >= 6 and (int(len)) <= 14:
        for _ in range(int(len)):
            generated_password += random.choice(chars)
        
    else:
        generated_password = "Not valid lenght..."
    

    return render(request, 'password.html', {'password': generated_password})
