from django.shortcuts import render

# Create your views here.
def ProfileHome(request):
    return render(request,'index.html')
