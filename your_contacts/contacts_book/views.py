from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user_contacts(request):
    return render(request, 'user_contacts.html')
