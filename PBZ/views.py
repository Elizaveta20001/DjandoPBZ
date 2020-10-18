from django.http import HttpResponseNotFound
from django.shortcuts import render
from PBZ.models import *
from django.shortcuts import HttpResponseRedirect
from django.db.models import Max
import datetime
import re


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
        context = {}
        product = Product.objects.get(id=product_id)
        context['product'] = product
        if request.method == "POST":
            if (request.POST["name_product"] == '' or request.POST["category"] == '' or request.POST["company"] == ''):
                context['error'] = True
                return render(request, 'edit.html', context)
            else:
                product.name = request.POST["name_product"]
                product.category = request.POST["category"]
                product.company = request.POST["company"]
                product.save()
                return HttpResponseRedirect("/edit_page")
        else:
            return render(request, "edit.html", context)
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


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


def create_context():
    context = {}
    temp = []
    temp_destination = []
    context['product'] = Product.objects.all()
    for i in Customer.objects.all():
        flag = True
        for j in Waybill.objects.all():
            if j.customer.id == i.id:
                flag = False
        if flag:
            temp.append(i)
    for i in Destination.objects.all():
        flag = True
        for j in Waybill.objects.all():
            if j.destination.id == i.id:
                flag = False
        if flag:
            temp_destination.append(i)

    context['customer'] = temp
    context['destination'] = temp_destination
    return context


def form_waybill(request):
    context = create_context()
    return render(request, 'form_waybill.html', context)


def form_customer(request):
    return render(request, 'form_customer.html', {})


def create_customer(request):
    if request.POST['type'] == '' or request.POST['name'] == '' or request.POST['address'] == '' or request.POST[
        'passport_id'] == '' or request.POST['passport_series'] == '' or request.POST['bank_details'] == '':
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
    return render(request, 'forn_destination.html', {})


def create_destination(request):
    if request.POST['country'] == '' or request.POST['region_name'] == '' or request.POST['street'] == '' or \
            request.POST['house_number'] == '' or request.POST['flat_number'] == '':
        context = {}
        context['error'] = True
        return render(request, 'forn_destination.html', context)
    else:
        country = request.POST['country']
        region_name = request.POST['region_name']
        street = request.POST['street']
        house_number = request.POST['house_number']
        flat_number = request.POST['flat_number']
        Destination(country=country, region_name=region_name, street=street, house_number=house_number,
                    flat_number=flat_number).save()
        return HttpResponseRedirect('/form_waybill')


def create_waybill(request):
    if request.POST['current_price'] == '' or request.POST['date'] == '' or request.POST['number_of_product'] == '':
        context = create_context()
        context['error'] = True
        return render(request, 'form_waybill.html', context)
    else:
        product = Product.objects.get(id=request.POST['product'])
        customer = Customer.objects.get(id=request.POST['customer'])
        current_price = request.POST['current_price']
        date = request.POST['date']
        number_of_product = request.POST['number_of_product']
        destination = Destination.objects.get(id=request.POST['destination'])
        Waybill(product=product, customer=customer, current_price=current_price, date=date,
                number_of_product=number_of_product, destination=destination).save()
        return HttpResponseRedirect('/page_waybill')


def show_customer(request):
    temp = []
    temp_sum = 0
    context = {}

    if request.method == 'POST':
        if request.POST['date'] == '':
            context['error'] = True
            return render(request, 'show_customer.html', context)
        else:
            try:
                for item in Waybill.objects.filter(date=request.POST['date']):
                    if temp_sum < item.number_of_product * item.current_price:
                        temp_sum = item.number_of_product * item.current_price
                    else:
                        continue
                for item in Waybill.objects.filter(date=request.POST['date']):
                    if temp_sum == item.number_of_product * item.current_price:
                        temp.append(item.customer)
            except:
                context['error'] = True
                return render(request, 'show_customer.html', context)
            else:
                context['customer'] = temp
                context['error'] = False
                return render(request, 'show_customer.html', context)


    else:
        context['error'] = False
        return render(request, 'show_customer.html', context)


def edit_waybill_page(request):
    context = {}
    context['waybill'] = Waybill.objects.all()
    return render(request, 'edit_waybill.html', context)


def edit_waybill(request, waybill_id):
    try:
        waybill = Waybill.objects.get(id=waybill_id)

        if request.method == "POST":
            waybill.product = request.POST["product"]
            waybill.customer = request.POST["customer"]
            waybill.current_price = request.POST[""]
            waybill.date = request.POST[""]
            waybill.number_of_product = request.POST[""]
            waybill.destination = request.POST[""]
            waybill.save()
            return HttpResponseRedirect("/edit_waybill_page")
        else:
            context = {}
            temp = []
            temp_destination = []
            context['product'] = Product.objects.all()
            for i in Customer.objects.all():
                flag = True
                for j in Waybill.objects.all():
                    if j.customer.id == i.id:
                        flag = False
                if flag:
                    temp.append(i)
            for i in Destination.objects.all():
                flag = True
                for j in Waybill.objects.all():
                    if j.destination.id == i.id:
                        flag = False
                if flag:
                    temp_destination.append(i)

            context['customer'] = temp
            context['destination'] = temp_destination
            return render(request, "form_for_edit_waybill.html", context)
    except Waybill.DoesNotExist:
        return HttpResponseNotFound("<h2>Waybill not found</h2>")


def page_delete_waybill(request):
    context = {}
    context['waybill'] = Waybill.objects.all()
    return render(request, 'delete_waybill.html', context)


def delete_waybill(request, waybill_id):
    try:
        waybill = Waybill.objects.get(id=waybill_id)
        waybill.delete()
        return HttpResponseRedirect('/delete_waybill_page')
    except Waybill.DoesNotExist:
        return HttpResponseNotFound("<h2>Waybill not found</h2>")


def show_price_change(request):
    context = {}
    temp = []
    if request.method == 'POST':
        if request.POST['first_date'] == '' or request.POST['last_date'] == '':
            context['error'] = True
            context['product'] = Product.objects.all()
            return render(request, 'show_price_change.html', context)
        else:
            try:
                for item in Waybill.objects.filter(product=request.POST['product']):
                    if item.date >= datetime.datetime.strptime(request.POST['first_date'],
                                                               '%Y-%m-%d').date() and item.date <= datetime.datetime.strptime(
                        request.POST['last_date'], '%Y-%m-%d').date():
                        temp.append(item)
            except:
                context['error'] = True
                context['product'] = Product.objects.all()
                return render(request,'show_price_change.html',context)
            else:
                context['error'] = False
                context['waybill'] = temp
                context['product'] = Product.objects.all()
                return render(request, 'show_price_change.html', context)
    else:
        context['error'] = False
        context['product'] = Product.objects.all()
        return render(request, 'show_price_change.html', context)
