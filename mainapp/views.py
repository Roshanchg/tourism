from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpRequest
from django.contrib.auth.decorators import login_required
from mainapp.models import Users
def loginForm(request):
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        alert_message="Email Or Pasword did not match !!"
        logged_user=''
        if(user_exists(email=email)):
            if (authenticate_user(email=email,password=password) is True):
                logged_user=get_name(email=email)
                userarr=logged_user.split(" ")
                temp=""
                for i in userarr:
                    print(i,userarr,logged_user)
                    temp+=i[0]
                logged_user=temp
                print(logged_user)
                return render(request=request,
                              template_name="mainapp/index.html",
                              context={'logged_user':logged_user})
            else:
                return render(request=request,template_name="mainapp/loginpage.html",context={'alert_message':alert_message})
    return render(request=request,template_name="mainapp/loginpage.html")

def registerForm(request):
    if request.method=='POST':
        name=request.POST.get("fullname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        alert_message="A User already exists with this email !!"
        if(not user_exists(email=email)):
            Users.objects.create(full_name=name,email=email,password=password)
            return redirect('/')
        return render(request=request,template_name="mainapp/loginpage.html",context={'alert_message':alert_message})
    return render(request=request,template_name="mainapp/loginpage.html")
    

def get_name(email):
    try:
        user=Users.objects.all().get(email=email)
        username=user.full_name
        return username
    except:
        return False
    

def authenticate_user(email, password):
    try:
        user=Users.objects.all().get(email=email)
        if user.password==password:
            return True
        else:
            return False
    except:
        return False
def user_exists(email):
    users=Users.objects.all()
    try:
        users.get(email=email)
        return True
    except Exception as e:
        print(e)
        return False

def mainPage(request):
    return render(request=request,template_name='mainapp/index.html')

def myaccount(request,email):
    if(user_exists(email=email)):
            name=get_name(email=email)
            userarr=name.split(" ")
            temp=""
            for i in userarr:
                temp+=i[0]
            return render(request=request,template_name='mainapp/accounts.html',context={'name':name,
                                                                                         'nameshort':temp,
                                                                                         'email':email,
                                                                                         'looping':[1,2,3,4,5]})
    return render(request=request,template_name="mainapp/loginpage.html")
