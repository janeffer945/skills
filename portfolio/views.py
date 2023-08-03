from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
   if request.method=="POST":
    name=request.POST.get('name')
    email=request.POST.get('email')
    phoneNo=request.POST.get('num')
    desc=request.POST.get('desc') 
    print(name,email,phoneNo,desc )
    messages.success()
    return redirect('/contact')
   



    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def resume(request):
    return render(request, 'resume.html')
