from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

# Create your views here.

def user_login_veiw(request):
    return render(request, "auth/user-login.html", {})

def user_register_view(request):
    form = check_for_user_registration(request)
    return render(request, "auth/user-register.html", {"form":form})
     
def admin_login_veiw(request):
    return render(request, "auth/admin-login.html", {})
    
def logout_view(request):
    logout(request)



def check_for_user_registration(request):
    
    if (request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if (form.is_valid()):
            print("form is valid")
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('create-view')
        else:
            print("form is not valid")
            messages.error(request, f'Form is not valid')
    else:
        print("form is not a POST ") 
        form = UserRegisterForm()
    
    return form

def check_for_user_login(request):
    if (request.method == 'POST'):
        form = UserLoginForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data.get('username')
            
            user = authenticate(request, username=username, password="")
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                messages.success(request, f'Hi {username}!')
                return redirect('create_view')
            else:
                # Return an 'invalid login' error message.
                messages.error(request, f"Could not log in with username '{username}''")
                    
    else: 
        form = UserLoginForm()
    
    return form

