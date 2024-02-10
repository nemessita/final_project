from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request):
    

    context = {
        'title': 'Home - Главная',
        'content': '',
        
        
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазин такой классныйб и какой клевый товары.'
        
    }
    return render(request, 'main/about.html', context)
