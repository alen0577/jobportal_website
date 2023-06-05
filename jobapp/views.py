from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def login(request): 
    
    return render(request,'login.html')

def loginuser(request):
    if request.method=='POST':
        username=request.POST['uname']  
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print(username,password)
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                print('1')
                return redirect('home')
            else:
                auth.login(request,user)
                print('2')
        
                return redirect('home') 
        else:

            print('last')             
            return redirect('/')
          

def register(request):
    if request.method=='POST':
        username=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        role=request.POST['role']
        first_name='none'
        last_name='none'
        user1=User.objects.create(email=email,password=password,first_name=first_name,last_name=last_name,username=username)
        user1.save()
        data=User.objects.get(id=user1.id)
        extdata=User1(user=data,radio_field=role)
        extdata.save()
        return redirect('/')

    return render(request,'register.html')    



def logout(request):
    auth.logout(request)
   
    return redirect('/')


def  home(request):
    return render(request, 'Jobseeker/home.html')