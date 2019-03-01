from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import  TimeCardForm
from .models import TimeCard
# Create your views here.



# my test page to see if it will run
#def index(request):
 #   return HttpResponse('call me')


# to display on my time frame

def index(request):
    time = TimeCard.objects.all()
    context = {
        'time': time

    }
    return render(request,'mini_app/index.html',context)