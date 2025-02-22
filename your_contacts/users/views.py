from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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

    return render(request, 'users/register_user.html', {"form": form})