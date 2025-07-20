from django.contrib import admin
from .models import Event , Venue , MyclubUser

# Register your models here.
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(MyclubUser)