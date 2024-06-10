from django.urls import path
from .views import *


urlpatterns = [
    path('', main_page),
    path('second/', second_page),
    path('therd/', therd_page),
    path('4th/', fourth_page),
    path('5th/', fifth_page),
    path('6th/', sixth_page),
    path('7th/', seventh_page),
    path('8th/', eighth_page),
    path('9th/', ninth_page),
    path('10th/', tenth_page),
    path('11th/', eleventh_page),
    path('form/', form),
]



