from django.shortcuts import render
from PBZ.models import *
from django.shortcuts import HttpResponseRedirect


def home_page(request):
    return render(request, 'home_page.html', {})

def page_product(request):
    return render(request,'page_product.html',{})