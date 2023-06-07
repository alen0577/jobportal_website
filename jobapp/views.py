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
                return redirect('employerhome')
            else:
                auth.login(request,user)
                print('2')
        
                return redirect('employerhome') 
        else:

            print('last')             
            return redirect('home')
          

def register(request):
    if request.method=='POST':
        username=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        role=request.POST['role']
        first_name='none'
        last_name='none'
        user1=User.objects.create_user(email=email,password=password,first_name=first_name,last_name=last_name,username=username)
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


def employerhome(request):
    return render(request,'Employer/employerhome.html')    


def jobdetails(request):
    return render(request,'Jobseeker/jobdetails.html')    

def alljobs(request):
    return render(request,'Jobseeker/alljobs.html')    


def notifications(request):
    return render(request,'Jobseeker/notifications.html')    

def profile(request):
    return render(request,'Jobseeker/profile.html')

def editprofile(request):
    return render(request,'Jobseeker/editprofile.html')    


def messages(request):
    return render(request,'Jobseeker/messages.html')  

def myjobs(request):
    return render(request,'Jobseeker/myjobs.html')         

def postjob(request):
    return render(request,'Employer/postjob.html')      

def empprofile(request):
    return render(request,'Employer/profile.html')    

def empeditprofile(request):
    return render(request,'Employer/editprofile.html')   

def empjobdetails(request):
    return render(request,'Employer/jobdetails.html') 

def jobupdate(request):
    return render(request,'Employer/jobupdate.html')  

def applicants(request):
    return render(request,'Employer/table.html')  

def empmessages(request):
    return render(request,'Employer/messages.html')                     