from django.shortcuts import render
from django.http import HttpResponse
from .models import Prime

# Create your views here.
def home(request):
    prime_data=Prime.objects.all()
    return render(request,"home.html",{"prime_data":prime_data})

def prime(request):
    prime_data=Prime.objects.all().order_by("-created_on")[0:4]
    print(prime_data.values())
    return render(request,"prime.html",{"prime_data":prime_data})

def details(request,id):
    single_blog_data=Prime.objects.filter(pk=id)
    print(single_blog_data.values())
    return render(request,"details.html",{"single_blog_data":single_blog_data})

