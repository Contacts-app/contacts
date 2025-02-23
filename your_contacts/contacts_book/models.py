from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Contacts_list(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Contact(models.Model):
    contacts_list = models.ForeignKey(Contacts_list,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.TextField(max_length=300, blank=True)
    telephone_number = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

# Create a contact list when the user is created
@receiver(post_save, sender=User)
def create_user_contacts_list(sender, instance, created, **kwargs):
    if created:
        Contacts_list.objects.create(user=instance)

#Update contacts list when user is updated
@receiver(post_save, sender=User)
def save_user_contact_list(sender, instance, **kwargs):
    instance.contacts_list.save()
