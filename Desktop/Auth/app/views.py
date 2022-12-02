from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *

#Start of Sign up System
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#Home Page
def home(request):
    return render(request, "index.html")

#Add Student Page
def add_student(request):
    form = StudentForm(request.POST or None)
    # customer = Student.objects.all()
    if form.is_valid():
        form.save()
    return render(request,"add.html", {"form":form})

#Show Student Details Page
def show_student(request):
    student = Student.objects.all()
    return render(request,"show.html",{"student":student})

#Update Student's Info Page
def update_student(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("update_student/<student_id>")
    return render(request,"update.html",{"student":student})
    
#Delete Student's Page
def delete_student(request,pk):
    form = Student.objects.get(id=pk)
    form.delete()
    return HttpResponseRedirect("/")


#START OF Sign UP, LOGIN/OUT CODE

#Sign up Page
def sign_up(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('signup')
    student = {"form": form}
    return render(request, "signup.html", student)

#Login in Page
def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
    context = {}
    return render(request, "login.html", context)

#Log out Page
def log_out(request):
    logout(request)
    return redirect("logout")
