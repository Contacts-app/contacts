from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from . import models

# Create your views here.
def home(request):
    return render(request, 'home.html')

class ViewContacts_view(LoginRequiredMixin, ListView):
    context_object_name = 'contacts_list' 
    model = models.Contact
    template_name = 'contacts_book/view_all_contacts.html'
    paginate_by = 5
    
    def get_queryset(self):
        # Get the Contacts_list instance for the current user
        c_list = models.Contacts_list.objects.get(user=self.request.user)
        # Filter contacts by the retrieved Contacts_list instance
        queryset = models.Contact.objects.filter(contacts_list=c_list)
        return queryset
