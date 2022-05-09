from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User

from .models import Profile

# @receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    print("profile Created")
    print('Instance:', instance)
    print('created:', created)
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )
        # profile.save()


# @receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    print('User delete')
    print('Instance:', instance)
    user = instance.user
    user.delete()
    
post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)