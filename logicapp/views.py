from django.shortcuts import render
from django.http import HttpResponse
from logicapp.models import *
from django import forms
from logicapp import form

# Create your views here.
def Home(request):
    return render(request,"HomePage.html",{})


#ADMIN OPERATION WILL BE DONE HERE

def AdminLogin(request):
    form_var = form.AdminLogin()

    if(request.method == "POST"):
        form_var = form.AdminLogin(request.POST)
        if(form_var.is_valid()):
            Login_ID1 = request.POST["Login_ID"]
            Password1 = request.POST["Password"]

            data = AdminDetails.objects.filter(Admin_Id=Login_ID1).all()
            for i in data:
                Admin_Id = i.Admin_Id
                Password = i.Password
                if(Admin_Id == Login_ID1 and Password == Password1):
                    count = AddLeads.objects.count()
                    return render(request,"AdminDashBoard.html",{'count':count})
                else:
                    return HttpResponse("The Login ID and Password that you Entered are Wrong")
        else:
            return HttpResponse("The form fields are not valid")
    return render(request,"AdminLogin.html",{'form':form_var})


def AdminDashBoard(request):
    return render(request,"AdminDashBoard.html",{})

def AddLead(request):
    form_var = form.AddLeads()
    if(request.method == "POST"):
        form_var = form.AddLeads(request.POST)

        if(form_var.is_valid()):
            form_var.save(commit = True)
            return render(request,"TrackLeads_Admin.html",{})
    return render(request,"AddLead_Admin.html",{'form':form_var})
def TrackLeads(request):
    data=AddLeads.objects.all()
    return render(request,"TrackLeads_Admin.html",{'form':data})
