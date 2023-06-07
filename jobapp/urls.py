from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('loginuser/>', views.loginuser, name='loginuser'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    path('employerhome/',views.employerhome,name='employerhome'),
    path('jobdetails/',views.jobdetails,name='jobdetails'),
    path('alljobs/',views.alljobs,name='alljobs'),
    path('notifications/',views.notifications,name='notifications'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('messages/',views.messages,name='messages'),
    path('myjobs/',views.myjobs,name='myjobs'),
    path('postjob/',views.postjob,name='postjob'),
    path('empprofile/',views.empprofile,name='empprofile'),
    path('empeditprofile/',views.empeditprofile,name='empeditprofile'),
    path('empjobdetails/',views.empjobdetails,name='empjobdetails'),
    path('jobupdate/',views.jobupdate,name='jobupdate'),
     path('applicants/',views.applicants,name='applicants'),
     path('empmessages/',views.empmessages,name='empmessages'),



]