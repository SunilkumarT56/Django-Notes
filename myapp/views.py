from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event , Venue , MyclubUser


def venues_list(request):
    venues = Venue.objects.all()
    return render(request , 'myapp/venue_list.html' , {'venues': venues})


def event_list(request):
    events = Event.objects.all()

    return render(request , 'myapp/events_list.html',  {'events': events})

def home(request,year=datetime.now().year,month=datetime.now().strftime("%B")):
    month = month.capitalize()
    name = "sunilkumar"
    month_number = list(calendar.month_name).index(month)
    now = datetime.now()
    now_year = now.year
    time = now.strftime("%I:%M %p" )
    cal = HTMLCalendar().formatmonth(year,month_number)
    return render(request , 'myapp/home.html',{
        "name":name,
        "year":year,
        "month":month,
        "month_number":month_number,
        "cal":cal,
        "now_year":now_year,
        "time":time,
    })
