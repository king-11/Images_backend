from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Not Say'),
)


class photographer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instaHandle = models.URLField(null=True, blank=True)
    home = models.CharField(max_length=255, null=True, blank=True)
    instituition = models.CharField(max_length=255, null=True, blank=True)
    profile_pic = models.URLField(null=True, blank=True)
    member = models.BooleanField(default=False)
    bio = models.TextField(max_length=255, null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default='Male')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_photographer_profile(sender, instance=None, created=False, **kwargs):
    if created:
        photographer.objects.get_or_create(user=instance)


class images(models.Model):
    link = models.URLField(unique=True)
    verified = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    person = models.ForeignKey(photographer, on_delete=models.CASCADE)
    place = models.CharField(
        max_length=100, blank=True, default=' ')
    tag = models.TextField(max_length=255, blank=True, default=' ')

    def __str__(self):
        return f'clicked at {self.place} by {self.person.user.username}'
# Create your models here.
