from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.
from django.http import HttpResponse

def index(request):
	imprimir= ("Hello, world. You're at the poll index.")
	return render(request, 'system/index.htm')