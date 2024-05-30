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
]



