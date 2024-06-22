from django.shortcuts import render
from .models import *
# Create your views here.
def main_page(request):
    p1 = First_page.objects.all()
    p1_img=p1[0].img
    p2 = Second_page.objects.all()
    p4=Fourth_page.objects.all()
    p8 = Eighth_page.objects.all()
    p10 = Ten_page.objects.all()
    p4title=p4[0].title
    title8=p8[0].p8title
    content8=p8[0].p8content
    img8=p8[0].p8image
    footer8=p8[0].p8footer
    p9 = Nine_page.objects.all()
    context = { 'page1' : p1, 'page2': p2, 'page4':p4, 'p1_img':p1_img, 'p4title':p4title, 'title':title8, 'p8_img':img8, 'content':content8, 'footer':footer8, 'page8':p8, 'page9':p9, 'page10':p10 }
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

def eighth_page(request):
    p8=Eighth_page.objects.all()
    title8=p8[0].p8title
    content8=p8[0].p8content
    img8=p8[0].p8image
    footer8=p8[0].p8footer
    context={'page8':p8, 'title':title8, 'img':img8, 'content':content8, 'footer':footer8 }
    return render(request, 'catalog/8th_page.html', context)

def ninth_page(request):
    p9=Nine_page.objects.all()
    p9_1img=p9[0].p9_1
    content={'page9':p9, 'p9img1':p9_1img }
    return render(request, 'catalog/9th_page.html', content)

def object_page(request, object):
    portfolio=Nine_page.objects.get(p9_title=object)
    content={'object':portfolio}
    return render(request, 'catalog/portfolio.html', content)

def object_photo_page(request, object, photo):
    portfolio2=Nine_page.objects.get(p9_title=object)
    content={'portfolio2':portfolio2, 'photo':photo}
    return render(request, 'catalog/object_photo.html', content)

def tenth_page(request):
    p10=Ten_page.objects.all()
    content={'page10':p10}
    return render(request, 'catalog/10th_page.html', content)

def eleventh_page(request):
    return render(request, 'catalog/11th_page.html')

def form(request):
    return render(request, 'catalog/form.html')