from django.shortcuts import render
from .models import DetailsModel

import random,qrcode
# Create your views here.
num=0

def register(request):
    return render(request,"register.html")

def register_details(request):
    Username = request.POST.get('t1')
    Password = request.POST.get('t2')
    DetailsModel(username=Username,password=Password).save()
    return render(request,"login.html",{"message":"successfully register"})

def login_page(request):
    return render(request,"login.html")

def validate_login(request):
    Username=request.POST.get('t1')
    Password=request.POST.get('t2')
    try:
        DetailsModel.objects.get(username=Username,password=Password)

        x=random.randint(10000,99999)
        global num
        num=x
        y=qrcode.make("Your OTP is "+str(x))
        y.save(r"app/static/image/one.jpg")
        return render(request,"qrcode.html")
    except DetailsModel.DoesNotExist:
        return render(request, "login.html",{"message":"invalid User"})

def otpvalidation(request):
    otp=request.POST.get("otp")
    # print(otp)
    # print(num)
    if int(otp) == num:
        return render(request, "welcome.html")
    else:
        return render(request, "login.html", {"message": "invalid OTP"})





