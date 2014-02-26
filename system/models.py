#!/usr/bin/env 
#-*- encoding: -utf-8-*-


from django.db import models

# Aqui creo las tablas:

class Alumno(models.Model):

	def __unicode__(self):  
		return self.matricula

	nombre = models.CharField(max_length=20)
	nom_paterno= models.CharField(max_length=20)
	nom_materno= models.CharField(max_length=20)
	matricula= models.CharField(max_length=10)
	fecha_alta = models.DateTimeField('Inicio')
	contrasena= models.CharField(max_length=30)

class Ruta(models.Model):
	def __unicode__(self):  
		return self.nombre
	nombre=models.CharField(max_length=40)
	salida=models.TimeField("Hora Salida")
	llegada= models.TimeField("Hora Llegada")
	distancia= models.IntegerField(max_length=5)
