from django.shortcuts import render,redirect 
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
def homeView(request):
    return render(request, 'home.html') 

# prince
# asdfg

def registerView(request):
    if request.user.is_authenticated:
        return redirect('../home')
    # restricting logged in users from redirecting to login page.
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect('/')
            messages.error(request, "unsuccessful registration. Invalid username or password!!")    
        context = {
            'form': form,
        }
        return render(request, 'register.html', context)

            

    

def loginView(request):
    # restriction to goto login page for logged in users.
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('../home')
            else:
                messages.info(request, "Invalid username or password!!")
            print(username)
            print(password)
        else:
            messages.info(request, "Invalid username or password!!")
    context = {
        'form':form,
    }
    return render(request, 'login.html', context)


def logoutView(request):
    auth.logout(request)
    messages.info(request, "Successfully logged out!")
    return redirect('/')

@login_required(login_url='login')
def formView(request):
    
    if request.method == 'POST':
        department = request.POST['department']
        cleared_by = request.POST['cleared_by']
        date = request.POST['date']
        clearance = request.POST['clearance']
        sign = request.POST['sign']
        
        new = clearanceModel(department=department, cleared_by=cleared_by, date=date, clearance=clearance, sign=sign, user=request.user)
        new.save()
        return render(request, 'form.html')
    else:
        return render(request, 'form.html')
    
# list view
@login_required(login_url='login')
def listView(request):
    log_user = request.user
    clearanceModels = clearanceModel.objects.filter(user=log_user)
    context = {
        'clearanceModels': clearanceModels
    }
    return render(request, 'formList.html', context)

