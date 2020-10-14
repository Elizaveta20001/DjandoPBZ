from django.http import HttpResponseNotFound
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
def edit_page(request):
    context = {}
    context['product'] = Product.objects.all()
    return render(request,'edit_page.html',context)

def edit_product(request,product_id):
    try:
        product = Product.objects.get(id=product_id)

        if request.method == "POST":
            product.name = request.POST["name_product"]
            product.category = request.POST["category"]
            product.company = request.POST["company"]
            product.save()
            return HttpResponseRedirect("/edit_page")
        else:
            return render(request, "edit.html", {"product": product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def delete_page(request):
    context = {}
    context['product'] = Product.objects.all()
    return render(request,'delete_page.html',context)

def delete_product(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return HttpResponseRedirect('/delete_page')
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")