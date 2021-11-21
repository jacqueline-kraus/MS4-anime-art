from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) # a user can only have one account
    default_street_address = models.CharField(max_length=80, null=True, blank=False)
    default_city = models.CharField(max_length=40, null=True, blank=False)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='select country', null=True, blank=False)
    
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile 
    instance.userprofile.save()
