from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'va'})
def add(request):
    val1=int(request.POST['n1'])
    val2=int(request.POST['n2'])
    r=val1+val2
    return render(request,'result.html',{'result':r})