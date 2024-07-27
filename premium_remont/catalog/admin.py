from django.contrib import admin
from . import models
# Register your models here.

#Регистрация моделей в admin.site для того чтобы была возможность работы с ними в административной панели
admin.site.register(models.First_page) #регистрация модели First_page в административной панели
admin.site.register(models.Second_page) #регистрация модели Second_page в административной панели
admin.site.register(models.Fourth_page) #регистрация модели Fourth_page в административной панели
admin.site.register(models.Eighth_page)
admin.site.register(models.Nine_page)
admin.site.register(models.Ten_page)
admin.site.register(models.Photo)
admin.site.register(models.Form)
