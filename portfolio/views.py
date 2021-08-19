from .models import Contact
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return HttpResponse("<h1>Thank you for reaching out to us we will get back to you shortly</h1>")
    return render(request, 'home.html')