from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("<H2> Hello Innocent Boy!!!</H2>")
