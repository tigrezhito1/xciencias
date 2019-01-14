from django.contrib import admin

from .models import Question

from polls.models import *

admin.site.register(Question)

@admin.register(Xiencias)
class XienciasAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	list_filter=('nombre',)


@admin.register(Jjss)
class XienciasAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	list_filter=('nombre',)

@admin.register(Mcks)
class XienciasAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	list_filter=('nombre',)

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	list_filter=('nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	list_filter=('nombre',)


@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
	list_display = ('id','fecha','tipo','categoria','descripcion')
	list_filter=('tipo',)




