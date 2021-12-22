from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team

def index(request):
    # obj = place.objects.all()
    obj1 = team.objects.all()
    return render(request, 'index.html',{'tm':obj1})
# Create your views here.

