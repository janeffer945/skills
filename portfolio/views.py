from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Blogs
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.message import EmailMessage
from django.core import mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from decouple import config


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        phoneno = request.POST.get("num")
        desc = request.POST.get("desc")

        # Save the contact to the database
        query = Contact(name=fname, email=femail, phonenumber=phoneno, description=desc)
        query.save()

        # Send email
        subject = "New Contact Submission - Web form"
        message = f"A new contact has been submitted:\n\nName: {fname}\nEmail: {femail}\nPhone: {phoneno}\nDescription: {desc}"
        from_email = config("EMAIL_HOST_USER")
        recipient_list = ["lastcam00@gmail.com"]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        messages.info(
            request, "Thanks for reaching out. We will get back to you soon..."
        )

        return redirect("/contact")  # Redirect to the 'contact' view

    return render(request, "contact.html")


def blog(request):
    posts = Blogs.objects.all()
    context = {"posts": posts}
    return render(request, "blog.html", context)


def resume(request):
    return render(request, "resume.html")
