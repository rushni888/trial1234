from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('''Congratulations, 
		You have created a web application
		using django''')
