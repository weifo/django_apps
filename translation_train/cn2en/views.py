from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Trans
import random

# Create your views here.
def index(request):
    # return render(request,'<h3>welcome to my website</h3>')
    tests=Trans.objects.filter(test_time=0)
    # sample=get_object_or_404(Trans,id=3)
    sample=Trans.objects.get(id=5)
    return render(request,'drill.html',{'test':tests,'sample':sample})

def test(request,request_id):
    try:
        # current=get_object_or_404(Trans,id=request_id)
        current=Trans.objects.get(id=request_id)
    except Trans.DoesNotExist:
        raise Http404('out of range！！')

    wordlist=current.english.split(' ')
    count=len(wordlist)
    if count<=3:
        tofill=['']*count
    else:
        # skip=['a','the','of','make','give','for','new','and','in','way']
        tofill=['' if len(x)>8 else x for x in wordlist]
        tofill[random.randint(0,count-1)]=''
    return render(request,'drill.html',{'tests':[],'sample':current,'tofill':tofill})


