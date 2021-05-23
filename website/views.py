#  hello/views.py
import datetime
from django.shortcuts import render

def home_page_view(request):
	context = {'time' : datetime.datetime.now()}
	return render(request, 'website/Home.html', context)

def page_one_view(request):
    return render(request, 'website/Template2.html')


def page_two_view(request):
    return render(request, 'website/Template3.html')

