from django.contrib import admin

# Register your models here.
from .models import Contacts_list, Contact


class Contact_admin(admin.ModelAdmin):
     list_display = ('name', 'address', 'telephone_number', 'email' )

admin.site.register(Contacts_list)
admin.site.register(Contact, Contact_admin)
