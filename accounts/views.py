from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USER NAME TAKEN")
                print("username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "EMAIL TAKEN")
                print("email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email,
                                                password=password1)
                user.save()
                print("user created")
        else:
            print("password not matched")
        return redirect('/')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
