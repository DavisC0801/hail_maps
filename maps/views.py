from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Client

def index(request):
    client_list = Client.objects.order_by('name')[:5]
    context = { 'client_list': client_list }
    return render(request, 'index.html', context)
