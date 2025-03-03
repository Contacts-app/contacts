from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def register_user_view(request):
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True
            return render(request, "users/register_user.html", {'registered' : registered})
    else:
        form = UserCreationForm()

    return render(request, 'users/register_user.html', {"form": form, 'registered' : registered})

def login_view(request): 
    logged_in =False
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logged_in = True
            return render(request, "users/login.html", {"logged_in": logged_in})
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {"form": form, "logged_in": logged_in})

def logout_view(request):
    was_logged_in = False
    if request.method == 'POST' and request.user.is_authenticated:
        logout(request)
        was_logged_in = True

    return render(request, "users/logout.html", {"was_logged_in": was_logged_in})

        