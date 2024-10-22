from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    firstname = models.CharField(max_length=50, null=True, blank=True, verbose_name="First Name") # First Name Display
    lastname = models.CharField(max_length=50, null=True, blank=True, verbose_name="Last Name") # Last Name Display
    about = models.TextField(blank=True, null=True)
    classes = models.TextField(blank=True, null=True, verbose_name="Classes You Would Teach (i.e CSCI152, CSCI232, CSCI315E): ")
    weekDayAvailable = models.CharField(max_length=50, null=True, blank=True, verbose_name="Week Days Available (i.e. Mondays, Wednesdays, Fridays):" )
    hourAvailable = models.CharField(max_length=50, null=True, blank=True, verbose_name="Hours Available (i.e 2:00 PM - 3:00 PM): ")
    
