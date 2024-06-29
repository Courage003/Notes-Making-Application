from django .shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def userlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['eid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    
                    
    return render(request, 'login_admin.html', d)


def signup1(request):
    error = ""
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        p = request.POST['ph']
        e = request.POST['emailid']
        pa = request.POST['password']
        b = request.POST['branch']
        r = request.POST['role']

        try:
            user = User.objects.create_user(username=e, password=pa, fname =f,lname=l)
            Signup.objects.create(user=user, ph=p, branch=b, role=r)
            error="no"
        except Exception as ex:
            print(ex)
            error="yes"    
    d={'error':error}        

    return render(request, 'signup.html',d)

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    return render(request, 'admin_home.html')

def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    #login nhi kiya toh vaapis ajaao login page par
    

    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user= user)
    d = {'data': data, 'user':user}
    return render(request, 'profile.html', d)