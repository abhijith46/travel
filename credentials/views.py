from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        passw=request.POST['password']
        user=auth.authenticate(username=uname,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        passw=request.POST['password']
        cpassw=request.POST['cpassword']
        if passw==cpassw:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"user already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=passw,first_name=fname,last_name=lname,email=email)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request, "password mismatched")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
