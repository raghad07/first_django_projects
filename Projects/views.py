from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Products
from django.shortcuts import get_object_or_404

def home(request:HttpRequest,id:int):

    #Products.objects.create(name='product1',price=100)
    #products = Products.objects.filter(id=id)
    products = get_object_or_404(Products,id=id)

    return HttpResponse(products)
   

def handler404(request,expection):
    return HttpResponse('Not Found 404 error',status=404)

    