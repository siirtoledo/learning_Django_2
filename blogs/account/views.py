from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def signup(request):
    print("hello world")
    if request.method =="POST":
        print("Hi how are you")
        firstName=request.POST["firstName"]
        # print(firstName)
        lastName=request.POST["lastName"]
        print(lastName)
        email=request.POST["email"]
        print(email)
        username=request.POST["username"]
        print(username)
        mobile=request.POST["mobile"]
        print(mobile)
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]
        email_word="@gmail.com"
        if  not (email.endswith(email_word)):
            messages.warning(request,"Registration Failed. Please use Student Email")
            return redirect("signup")
        if password != confirm_password:
            # print("Password does not match")
            messages.error(request,"password does not match")
            return redirect("signup")
        if len(password) < 8:
            messages.error(request,"Please password is too short")
            return redirect("signup")
        
        # print(password)
        
        # print(firstName,lastName,email,username,mobile,password,confirm_password)
        user= User.objects.create_user(first_name=firstName,last_name=lastName,email=email,username=username,password=password)
        try:
            
            user.save()
            print(username,email)

            messages.success(request,"Registration Successful Login Now")
            return redirect("login")
        except:
           
           messages.error(request,"Registration Failed")
           return redirect("signup")
    
    return render(request,"signup.html")


def login(request):
    if request.method == "POST":
        username=request.POST["username"]
    
        password=request.POST["password"]
        user= auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(request,user)
          
          print(username,password)
          messages.success(request,f"Welcome {user.first_name} your Login was Successful")
          return redirect("home")
        else:
            messages.error(request,"Login failed, wrong username or password!")
            return redirect("login")

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("login")