from turtle import update
from django.http import JsonResponse
from .models import Store
import csv, io
from django.shortcuts import render
from django.contrib import messages
from dateutil import parser
from django.db import IntegrityError
q = Store.objects.all()

def storeData_upload(request):    
    files = request.FILES.getlist('file') 
    try:  
        for f in files:
            csv_file = f
            if not csv_file.name.endswith('.csv'):
                return render(request, "csvUpload.html", {"message": 'MAKE SURE YOU ARE UPLOADING A CSV FILE ONLY'})
            else:
                data_set = csv_file.read().decode('UTF-8')    
                io_string = io.StringIO(data_set)
                next(io_string)        
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    _, created = Store.objects.update_or_create(
                        storeId=column[0],
                        sku=column[1],
                        productName=column[2],
                        price=column[3],
                        date=column[4]
                    )
    except IntegrityError as e:
        return render(request, "csvUpload.html", {"message": 'Upload csv with unique store ids.'})
    storeFromDatabase = Store.objects.all()
    template = "csvUpload.html"
    context={}
    context['headers'] = ['StoreId', 'SKU','Product Name','Price', 'Date']
    context['data'] = storeFromDatabase
    return render(request, template, context)

def filterData(request, id):
    global q
    template = "csvUpload.html"
    context={}
    context['headers'] = ['StoreId', 'SKU','Product Name','Price', 'Date']
    if (id==1):
        q = Store.objects.all()
        if request.method == 'GET':
            storeIdSearch = request.GET.get('storeIdSearc')        
            if (storeIdSearch != ''):
                q = q.filter(storeId = storeIdSearch)
            skuSearch = request.GET.get('skuSearch',None)           
            if (skuSearch != ''):
                q = q.filter(sku = skuSearch)
            productNameSearch = request.GET.get('productNameSearch',None)
            if (productNameSearch != ''):
                q = q.filter(productName = productNameSearch)
            priceSearch = request.GET.get('priceSearch',None)
            if (priceSearch != ''):
                q = q.filter(price = priceSearch)
            dateSearch = request.GET.get('dateSearch',None)
            if (dateSearch != ''):
                dateSearch = parser.parse(dateSearch)
                dateSearch = dateSearch.strftime("%Y-%m-%d")
                q = q.filter(date = dateSearch)        
        context['data'] = q
        return render(request, template, context)
    else:
        context['data'] = q
        return render(request, template, context)

def saveStoreData(request,id):
    editedStore = Store.objects.get(storeId=id)
    if request.method=='GET': 
        editedStore.sku = request.GET.get('sku')
        editedStore.productName = request.GET.get('productName')
        editedStore.price = request.GET.get('price')
        editedDate = parser.parse(request.GET.get('date'))
        editedStore.date = editedDate.strftime("%Y-%m-%d")
        editedStore.save()
        return JsonResponse({'response':'success'})