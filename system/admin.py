from django.contrib import admin
from system.models import Alumno,Ruta
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'nom_paterno', 'nom_materno', 'matricula')
	list_filter=['matricula']

class RutaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'distancia')

admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Ruta,RutaAdmin)

