from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Switches
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'controlapp/index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exits try something else")
            return redirect('signup')
        
        if User.objects.filter(email=email):
            messages.error(request, "An account with this email exits")
            return redirect('signin')

        if pass1 != pass2:
            messages.error(request, "password doesn't match")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        s = Switches(username=username)
        s.save()

        messages.success(request, 'Your account has been successfuly created')
        return redirect('signin')
    return render(request, 'controlapp/signup.html')

def signin(request):
    if request.method == 'POST' and 'signin' in request.POST:
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # current_user = request.user
            # name = current_user.username
            name = user.username

            status = Switches.objects.get(username=name)
                
            return render(request, 'controlapp/index.html', {'name': name, 'status':status})
        else:
            messages.error(request, 'Bad credentials')
            return redirect('home')
    if request.user.is_authenticated:
        current_user = request.user
        name = current_user.username
        status = Switches.objects.get(username=name)

        if request.method == 'POST' and 'sw1' in request.POST:
            status.switch_1 = not status.switch_1
            status.save()
        if request.method == 'POST' and 'sw2' in request.POST:
            status.switch_2 = not status.switch_2
            status.save()
        if request.method == 'POST' and 'sw3' in request.POST:
            status.switch_3 = not status.switch_3
            status.save()
        if request.method == 'POST' and 'sw4' in request.POST:
            status.switch_4 = not status.switch_4
            status.save()
        if request.method == 'POST' and 'sw5' in request.POST:
            status.switch_5 = not status.switch_5
            status.save()
            
        return render(request, 'controlapp/index.html', {'name': name, 'status':status})



    return render(request, 'controlapp/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('home')

def returnhome(request):
    return redirect('home')

