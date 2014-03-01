from django.contrib import admin
from system.models import Alumno, Ruta, RegistroEntrada,RegistroSalida, Camion
import base64
import datetime
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('nombre1', 'nombre2', 'ap_paterno', 'ap_materno', 'matricula','encriptado')
	list_filter=['matricula']

class RutaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'kilometraje','salida','llegada')

class RegEntradaAdmin(admin.ModelAdmin):
	list_display= ('id', 'fecha','latitud', 'longitud')
	list_filter=['fecha']

class RegSalidaAdmin(admin.ModelAdmin):
	list_display= ('id', 'fecha','latitud', 'longitud')
	list_filter=['fecha']

class CamionAdmin(admin.ModelAdmin):
	list_display=('nombre','placa', 'asientos', 'velocidad','latitud','longitud')
	list_filter=['nombre']

admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Ruta,RutaAdmin)
admin.site.register(RegistroSalida,RegSalidaAdmin)
admin.site.register(RegistroEntrada,RegEntradaAdmin)
admin.site.register(Camion,CamionAdmin)

