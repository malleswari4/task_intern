from django.shortcuts import render,redirect
from django.http import HttpResponse
from App.models import *
from App.forms import *
from Project import settings
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def index(request):
    return render(request,'App/index.html')
def login(request):
    if request.method=="POST":
        # email=request.POST['emailid']
        # upass=request.POST['pass']
        try:
            data=User_Register.objects.get(reg_email=request.POST['emailid'],reg_pass=request.POST['pass'])
            if data:
                 messages.success(request,"Logged Successfully")
            else:
                messages.error(request,"Login Failed")
        except Exception:
            return HttpResponse("Wrong Credentionals ...!!!")
      
    return render(request, 'App/login.html')
def signup(request):
    if request.method=="POST":
        fname=request.POST['username']
        femail=request.POST['email']
        faddress=request.POST['address']
        fpass=request.POST['password']
        details=User_Register(reg_name=fname,reg_email=femail,reg_address=faddress,reg_pass=fpass)
        details.save()
        messages.success(request,"Registered successfully")
    return render(request,'App/signup.html')
    messages.error(request,"Registered Failed")
    
def users(request):
    data=User_Register.objects.all()
    return render(request,'App/users.html',{'data':data})

def delete(request,pk):
    item=User_Register.objects.get(id=pk)
    item.delete()
    data=User_Register.objects.all()
    if request.method=='POST':
        messages.success(request,"Deleted successfully")
    
    return render(request,'App/users.html',{'data':data})

# def edit(request,pk):
#     item=User_Register.objects.get(id=pk)
#     data=User_Register.objects.all()
#     if request.method=='POST':
#         item.reg_name=request.POST['username']
#         item.reg_email=request.POST['usermail']
#         item.reg_address=request.POST['useraddress']
#         item.save()
#         return redirect('users')
        
#     return render(request,'App/users.html',{'data':data})

def edit(request, pk):
    item = User_Register.objects.get(id=pk)
    context = {'item': item}
    # item.reg_name=request.POST['name']
    # item.reg_email=request.POST['usermail']
    # item.reg_address=request.POST['useraddress']
    

    return render(request, 'App/edit.html', context)

def update(request, pk):
    data=User_Register.objects.all()
    item = User_Register.objects.get(id=pk)
    if request.method=="POST":
        item.reg_name=request.POST['name']
        item.reg_email=request.POST['usermail']
        item.reg_address=request.POST['useraddress']
        item.save()
    return render(request,'App/users.html',{'data':data})

def logout(request):
    if request.method=='POST':
        logout(request)
    return render(request,'App/index.html')