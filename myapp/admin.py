from django.contrib import admin
from .models import Event , Venue , MyclubUser

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    search_fields = ("title","event_date")
    fields = (("title","venue"),"event_date","description")
    list_display = ("title","venue","event_date","description")
    list_filter =("title","event_date")
    ordering = ("title",)

class VenueAdmin(admin.ModelAdmin):
    search_fields = ("name","zip_code")
    list_display = ("name","zip_code","email_address")
    list_filter = ("name","zip_code")
    ordering = ("name",)
     
class MyclubUserAdmin(admin.ModelAdmin):
    search_fields =("user",)
    list_display = ("user","phone")
    ordering = ("user",)
    



admin.site.register(Event,EventAdmin)
admin.site.register(Venue , VenueAdmin)
admin.site.register(MyclubUser)