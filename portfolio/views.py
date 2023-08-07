from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact,Blogs

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
   if request.method=="POST":
    name=request.POST.get('name')
    email=request.POST.get('email')
    phoneno=request.POST.get('num')
    desc=request.POST.get('desc') 
    query = Contact(name=name,email=email,phonenumber=phoneno,description=desc )
    query.save()
    messages.success(request, "Thanks for conctacting, I will get to you soon! ")
    return redirect('/contact')
   
    return render(request, 'contact.html')
   
def blog(request):
    return render(request, 'blog.html')

def resume(request):
    return render(request, 'resume.html')
