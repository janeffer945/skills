from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact,Blogs
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.message import EmailMessage
from django.core import mail
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        phoneno = request.POST.get('num')
        desc = request.POST.get('desc')

        query = Contact(name=fname, email=femail, phonenumber=phoneno, description=desc)
        query.save()
        messages.info(request, "Thanks for reaching to us we will get back to you soon...")


        
       
        return redirect('/contact')  # Redirect to the 'contact' view

    return render(request, 'contact.html')

def blog(request):
    posts=Blogs.objects.all()
    context={'posts':posts}
    return render(request, 'blog.html', context)

def resume(request):
    return render(request, 'resume.html')
