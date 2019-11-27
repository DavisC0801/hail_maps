from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Address

def index(request):
    address_list = Address.objects.order_by('zip')[:5]
    context = { 'address_list': address_list }
    return render(request, 'index.html', context)
