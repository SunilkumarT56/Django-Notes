from django.db import models
from django.contrib.auth.models import User


class MyclubUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Event(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateField()
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE , null = True , blank=True)  # Link here
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} at {self.venue}"

    
class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    email_address = models.EmailField(blank=True)

    def __str__(self):
        return self.name

