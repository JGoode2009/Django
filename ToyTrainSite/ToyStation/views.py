from django.shortcuts import render
from .models import Toy
# Create your views here.

def toy_list(request):
    toys = Toy.objects.all()
    return render(request, 'toys.html', {'toys': toys})