from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event , Venue , MyclubUser
from .forms import VenueForm , EventForm


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addevent?submitted=True')
    else:
        form = EventForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'myapp/add_event.html', {"form": form, "submitted": submitted})

def delete_event(request , event_id):
    event = Event.objects.get(id = event_id)
    event.delete()
    return redirect('event-list')

def update_event(request , event_id):
    event = Event.objects.get(id = event_id)
    form = EventForm(request.POST or None , instance = event)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        return render(request , 'myapp/update_event.html',{'form':form})

def delete_venue(request , venue_id):
    venue = Venue.objects.get(id=venue_id)
    venue.delete()
    return redirect('venues-list')

def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment ; filename = venue.txt'
    lines = [f"{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.website}\n{venue.email_address}\n\n\n" for venue in Venue.objects.all()]
    response.writelines(lines)
    return response

def update_venue(request , venue_id):
    venue_id = int(venue_id)
    venue = Venue.objects.get(id=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    
    if request.method == "POST":
      if form.is_valid():
          form.save()
          return redirect('venues-list')
    else:
        return render(request , 'myapp/update_venue.html',{'form':form})



def particular_venue(request , venue_id):
    venue_id = int(venue_id)
    venues = Venue.objects.get(id=venue_id)
    return render(request , 'myapp/particular_venue.html' , {'venues':venues})

def search_venue(request):
    result = False
    if request.method == "POST":
        searched = request.POST.get("searched")
        venues = Venue.objects.filter(name__icontains=searched)  # more flexible search
        if venues.exists():
            result = True
        return render(request, 'myapp/search_venue.html', {
            "searched": searched,
            "venues": venues,
            "result": result
        })
    else:
        return render(request, 'myapp/search_venue.html', {})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("addvenue?submitted=True")
    else:
        form = VenueForm
        if "submitted" in request.GET:
            submitted = True
    
    return render(request , 'myapp/add_venue.html',{"form":form,"submitted":submitted})
    

def venues_list(request):
    venues = Venue.objects.all().order_by("name")
    return render(request , 'myapp/venue_list.html' , {'venues': venues})


def event_list(request):
    events = Event.objects.all()

    return render(request , 'myapp/events_list.html',  {'events': events})

def nows(request,year=datetime.now().year,month=datetime.now().strftime("%B")):
    month = month.capitalize()
    name = "sunilkumar"
    month_number = list(calendar.month_name).index(month)
    now = datetime.now()
    now_year = now.year
    time = now.strftime("%I:%M %p" )
    cal = HTMLCalendar().formatmonth(year,month_number)
    return render(request , 'myapp/now.html',{
        "name":name,
        "year":year,
        "month":month,
        "month_number":month_number,
        "cal":cal,
        "now_year":now_year,
        "time":time,
    })
def home(request):
    return render(request , 'myapp/home.html' ,{})
