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
    content={'page9':p9, 'p9img1':p9_1img}
    return render(request, 'catalog/9th_page.html', content)

def object_page(request, object):
    photos = Photo.objects.filter(obect__p9_title=object) #Получакем выборку всех фото из модели Photo у которых obect соответсвеут
#параметру запроса object (obect__p9_title=object - означает что поле obect модели Photo, а соотвественно и связанное с ним имя поля
#модели Nine_page должны соответсвовать праметру запроса object
    #Далее закомментированный код тех же действий но сложнее - в 2 этапа
    # portfolio=Nine_page.objects.get(p9_title=object) # тут выбираем объект из модели Nine_page у которого
#поле p9_title соответсвует пришедщему из запроса параметру object. Присваем полученное значение некоторой переменной portfolio
    # imgs=portfolio.photo_set.all() # тут, используя объявленную выше переменную и параметр _set обращаемся
# к связанной с моделью Nine_page модели Photo и выбираем из неё все объекты у которых поле obect совпадают с
#объектом, указанны в переменной porfolio
    # # imgs=Nine_page.objects.filter(photo__obect=portfolio.pk) #здесь деламе тоже самое что и в предыдущей строке, но уже не через параметр set, а через фильтрацию
#объектов модели Nine_page по условию - поле obect связанной модели Photo (photo__obect) совпадает с полем pk у переменной portfolio
    # content={'object':portfolio, 'photos':photos, 'imgs':imgs }
    content = {'photos': photos, 'object':object}
    return render(request, 'catalog/portfolio.html', content)

def photo(request, object, pk): # функция отображения фотограции объекта при нажатии на нее в общем списке фото
    photos=Photo.objects.filter(obect__p9_title=object, pk=pk) # выбираем объект из модели Photo со следующим фильтром:
# поле obect модели Photo должно соответсвовать наименованию объекта из модели Nine_page с которой связана модель Photo
# т.е. равно параметру object пришедщему из запрос. Идентификатор записи должен соответсвовать параметру pk, который тоже
# приходит из запроса (второй параметр)
    portfolio = Nine_page.objects.get(p9_title=object) # Это второй способ выбора этогоже объекта, но в 2 этапа
# первым этапом выбирается объекта из модели Nine_page у которого поле p9_title соответсвует параметру object,
# пришедшшему из запроса. Этот объект присвается некой переменной,
# вторым этапом черем ранее определенную переменну обращаются к связанной можели Photo c помощью метода _set
# имя_перемен.имя_связ_модели_set и получают из неё объект, связанный с объектом определенным выше и у которого pk
# равен второму параметру из запроса pk. Эти все сложности нужны для того чтобы:
    #1. получить коллекцию объектов относящихся к определеннолму объекту и потом определить pk первого
    # и последнего элемента данной коллекции, чтобы в последующем сравнивать pk выбранных фото с ними
    # и определять являются ли они первым фото или последним и в зависимости от этого выводить или не
    # выводить стрелки/ссылки на следующее или предыдущее фото
    #2. опредеть pk выбранного фото, задать это значение некой переменной i, ввести ещё 2 переменные -
    # первую на 1 больше i+1, вторую на одно меньше i-1. Сравнивать исходную переменную с pk первой и
    # последней фото определенного объекта и в зависимости от сравнения давать ссылку с pk=i+1 или pk=i-1

    img = portfolio.photo_set.get(pk=pk) # тут поулчаем конкретный объект из модели Photo у которого pk=pk
    i = img.pk # получаем его pk и присваем его переменной i
    imgs=portfolio.photo_set.filter(obect__p9_title=object) # Получаем набор (коллекцию queryset из
    # модели Photo соответсвущую какому-то определенному объекту - все фото объекта object из запроса
    len_obect_photo_list=len(imgs) # вычисляем длину этой коллекции
    first_photo_obect=imgs[0] #берем первый элемент коллекции, присваеваем его значению переменной
    last_photo_obect=imgs[len_obect_photo_list-1] #берем первый элемент коллекции, присваеваем его значению переменной
    l=i-1 # переменная для сосдания ссылки на предыдущее фото
    r=i+1 # переменная для сосдания ссылки на следующее фото
    context={'photos':photos, 'img':img, 'portfolio':portfolio, 'l':l, 'r':r,
             'imgs':imgs, 'len_obl':len_obect_photo_list,
             'first_photo':first_photo_obect, 'last_photo':last_photo_obect
             }
    return render(request, 'catalog/photo.html', context)

#Это более простая функция выполняющая аналогичные действия предыдущей функции - выводящее фото при нажатии на него
#Тут всего 1 параметр вместо 2-х как в предыдущей функции. В действительности параметр pk модели Photo уникален
#и отловив его мы можем выбрать конкретное фото а не фильтровать сначала все фото по отношению к объекту.
# Но я оставлю предыдущую, более сложную функцию в работе т.к. у неё получается хоть и более сложный, но логичный
#и понятный путь '../<str:object>/<int:pk>' сначала указывается объект, потом номер фото. В то время как у функции
# ниже путь будет просто номер фото '../<int:pk>'
# def photo(request, pk): #отлавливаем параметр pk из запроса
#     photos=Photo.objects.filter(pk=pk) # выбираем объект из модели Photo у которого pk равно параметру pk из запроса
#     context={'photos':photos}
#     return render(request, 'catalog/photo.html', context)


def tenth_page(request):
    p10=Ten_page.objects.all()
    content={'page10':p10}
    return render(request, 'catalog/10th_page.html', content)

def eleventh_page(request):
    return render(request, 'catalog/11th_page.html')

def form(request):
    return render(request, 'catalog/form.html')