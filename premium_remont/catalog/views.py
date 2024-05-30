from django.shortcuts import render
from .models import *
# Create your views here.
def main_page(request):
    p1 = First_page.objects.all()
    p2 = Second_page.objects.all()
    p4=Fourth_page.objects.all()
    p4title=p4[0].title
    context = { 'page1' : p1, 'page2': p2, 'page4':p4, 'p4title':p4title}
    return render(request, 'catalog/main_page.html', context)

def second_page(request):
    p2 = Second_page.objects.all()
    context = { 'page2': p2 }
    return render(request, 'catalog/second_page.html', context)

def therd_page(request):
    return render(request, 'catalog/therd_page.html')

def fourth_page(request):
    p4=Fourth_page.objects.all()
    p4title=p4[0].title
    context={ 'page4':p4, 'p4title':p4title}
    return render(request, 'catalog/4th_page.html', context)

def fifth_page(request):
    return render(request, 'catalog/5th_page.html')

def sixth_page(request):
    return render(request, 'catalog/6th_page.html')

def seventh_page(request):
    return render(request, 'catalog/7th_page.html')