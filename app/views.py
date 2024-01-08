from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Data is Inserted')
        else:
            return HttpResponse('Invalid Data')
            
    return render(request,'insert_topic.html',d)




def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=="POST":
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('Webpage_Data is Inserted') 
        else:
            return HttpResponse('Invalid Data') 
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EARFO=AccessRecordform()
    d={'EARFO':EARFO}
    if request.method=="POST":
        ARFDO=AccessRecordform(request.POST)
        if ARFDO.is_valid():
            ARFDO.save()
            return HttpResponse('AccessRecord_Data is Inserted')             
        else:
            return HttpResponse('Invalid Data') 
    return render(request,'insert_accessrecord.html',d)


