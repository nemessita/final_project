from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def error_404(request,exception):
    return render(request, '404.html')
