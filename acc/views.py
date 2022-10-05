from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'acc/index.html')

def profile(request):
    return render(request, 'acc/profile.html')

def update(request):
    if request.method=="POST":
        u=request.user
        uemail=request.POST.get("mail")
        udesc=request.POST.get("desc")
        if request.FILES.get("pic"):
            upic=request.FILES.get("pic")
            u.pic.delete()
            u.email,u.email,u.pic=uemail,udesc,upic
        else:
            u.email,u.email=uemail,udesc
        u.save()
        return redirect("acc:profile")

    return render(request,"acc/update.html")

def delete(request):
    if request.method=="POST":
        p1=request.POST.get("cpwd")
        p2=request.user
        if check_password(p1,p2.password):
            request.user.delete()
            p2.pic.delete()
            return redirect("acc:index")
    return redirect("acc:profile")

def signup(request):
    if request.method=="POST":
        uid=request.POST.get("id")
        upwd=request.POST.get("pwd")
        udesc=request.POST.get("desc")
        upic=request.FILES.get("pic")
        try:
            User.objects.create_user(username=uid, password=upwd,comment=udesc,pic=upic)
        except:
            messages.info(request, "이미 존재하는 username입니다")
        return redirect("acc:login")
    return render(request,"acc/signup.html")

def userlogin(request):
    if request.method=="POST":
        id=request.POST.get("id")
        pwd=request.POST.get("pwd")
        u=authenticate(username=id,password=pwd)
        if u:
            login(request,u)
            messages.success(request, f"{id}님 환영합니다")
            return redirect("acc:index")
        else:
            messages.info(request, "계정정보가 일치하지 않습니다")
    return render(request,'acc/login.html')

def userlogout(request):
    logout(request)
    return redirect("acc:index")

def cgpwd(request):
    u=request.user
    p1=request.POST.get("cpwd")
    if check_password(p1,u.password):
        p2=request.POST.get("npwd")
        u.set_password(p2)
        u.save()
        return redirect("acc:login")
    else:
        messages.info(request, "패스워드가 일치하지 않습니다")
    return redirect('acc:update')

