from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=Username):
                messages.error(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.error(request,"Email already in Use")
                return redirect('register')
            else:    
                myuser = User.objects.create_user(Username,email,password1)
                myuser.first_name=f_name
                myuser.last_name=l_name
                myuser.save()
                messages.success(request,"Your Account has been successfully created.")
                return redirect('signin')
        else:
            messages.error(request,"Password Mismatch")
            return redirect('register')
    else:
        return render(request,'login.html')


def signin(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password1 = request.POST['pass1']
        user = authenticate(username=Username,password=password1)
        if user is not None:
            login(request, user)
            x=User.objects.get(username=Username)
            return render(request,'Useraccount.html',{'name': x.first_name+" "+x.last_name })
        else:
            messages.error(request,"Wrong Username or Password")
            return redirect('signin')
    else:
        return render(request,'login.html')
def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return render(request,'login.html')
    

   