from django.shortcuts import render
from PBZ.models import *
from django.shortcuts import HttpResponseRedirect


def home_page(request):
    return render(request, 'home_page.html', {})

def page_product(request):
    return render(request,'page_product.html',{})

def form_product(request):
    return render(request,'form_product.html',{})

def create_product(request):
    if request.POST['name_product'] == '' or request.POST['category'] == '' or request.POST['company'] == '':
        context = {}
        context['error'] = True
        return render(request,'form_product.html',context)
    else:
        name = request.POST['name_product']
        category = request.POST['category']
        company = request.POST['company']
        Product(name=name,category=category,company=company).save()
        return HttpResponseRedirect('/product_page')