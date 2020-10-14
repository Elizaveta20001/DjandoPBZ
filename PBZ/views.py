from django.http import HttpResponseNotFound
from django.shortcuts import render
from PBZ.models import *
from django.shortcuts import HttpResponseRedirect


def home_page(request):
    return render(request, 'home_page.html', {})


def page_product(request):
    return render(request, 'page_product.html', {})


def form_product(request):
    return render(request, 'form_product.html', {})


def create_product(request):
    if request.POST['name_product'] == '' or request.POST['category'] == '' or request.POST['company'] == '':
        context = {}
        context['error'] = True
        return render(request, 'form_product.html', context)
    else:
        name = request.POST['name_product']
        category = request.POST['category']
        company = request.POST['company']
        Product(name=name, category=category, company=company).save()
        return HttpResponseRedirect('/product_page')


def edit_page(request):
    context = {}
    context['product'] = Product.objects.all()
    return render(request, 'edit_page.html', context)


def edit_product(request, product_id):
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
    return render(request, 'delete_page.html', context)


def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return HttpResponseRedirect('/delete_page')
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def show_category_of_product(request):
    context = {}
    result = []
    temp = Product.objects.values('category').distinct()
    for x in temp:
        result.append(x['category'])

    context['product'] = result
    return render(request, 'show_category_of_product.html', context)


def page_waybill(request):
    return render(request, 'waybill.html', {})


def form_waybill(request):
    context = {}
    temp = []
    context['product'] = Product.objects.all()
    #for i in Waybill.objects.all():
       # flag = True
        #for j in Customer.objects.all():
         #   if i.customer == j:
           #     flag = False
           # if flag == True:
            #    temp.append(j)


    context['customer'] = Customer.objects.all()
    context['destination'] = Destination.objects.all()
    return render(request, 'form_waybill.html', context)


def form_customer(request):
    return render(request, 'form_customer.html', {})


def create_customer(request):
    if request.POST['type'] == '' or request.POST['name'] == '' or request.POST['address'] == '' or request.POST['passport_id'] == '' or request.POST['passport_series'] == ''  or request.POST['bank_details'] == '':
        context = {}
        context['error'] = True
        return render(request, 'form_customer.html', context)
    else:
        type = request.POST['type']
        name = request.POST['name']
        address = request.POST['address']
        passport_id = request.POST['passport_id']
        passport_series = request.POST['passport_series']
        bank_details = request.POST['bank_details']
        Customer(type=type, name=name, address=address, passport_id=passport_id, passport_series=passport_series,
                 bank_details=bank_details).save()
        return HttpResponseRedirect('/form_waybill')

def form_destination(request):
    return render(request,'forn_destination.html',{})

def create_destination(request):
    if request.POST['country'] == '' or request.POST['region_name'] == '' or request.POST['street'] == '' or request.POST['house_number'] == '' or request.POST['flat_number'] == '' :
        context = {}
        context['error'] = True
        return render(request, 'form_customer.html', context)
    else:
        country = request.POST['country']
        region_name = request.POST['region_name']
        street = request.POST['street']
        house_number = request.POST['house_number']
        flat_number = request.POST['flat_number']
        Destination(country=country, region_name=region_name, street=street, house_number=house_number, flat_number=flat_number).save()
        return HttpResponseRedirect('/form_waybill')

def create_waybill(request):
    if request.POST['current_price'] == '' or request.POST['date'] == '' or request.POST['number_of_product'] == '':
        context = {}
        context['error'] = True
        return render(request, 'form_waybill.html', context)
    else:
        product = Product.objects.get(id=request.POST['product'])
        customer = Customer.objects.get(id=request.POST['customer'])
        current_price = request.POST['current_price']
        date = request.POST['date']
        number_of_product = request.POST['number_of_product']
        destination = Destination.objects.get(id=request.POST['destination'])
        Waybill(product=product, customer=customer, current_price=current_price, date=date, number_of_product=number_of_product,destination=destination).save()
        return HttpResponseRedirect('/page_waybill')

