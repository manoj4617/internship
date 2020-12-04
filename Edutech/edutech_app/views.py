from django.shortcuts import render

def index(request):
    return render(request, 'edutech_app/homepage.html')
