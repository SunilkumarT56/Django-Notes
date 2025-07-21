from django.urls import path
from .import views

urlpatterns = [
    path('',views.home , name='home'),
    path('<int:year>/<str:month>/',views.nows , name='now'),
    path('events',views.event_list , name = 'event-list'),
    path('venues',views.venues_list , name='venues-list'),
    path('addvenue',views.add_venue , name='add-venue'),
    path('searchVenue',views.search_venue , name='search-venue'),
    path('venue/<int:venue_id>/',views.particular_venue , name='particular-venue'),
    path('update_venue/<int:venue_id>/',views.update_venue , name='update-venue'),
    path('venuetextfile',views.venue_text , name='venue-text'),
    path('delete_venue/<int:venue_id>/',views.delete_venue , name='delete-venue'),
    path('update_event/<int:event_id>/',views.update_event , name='update-event'),
    path('delete_event/<int:event_id>/',views.delete_event , name='delete-event'),
    path('addevent',views.add_event , name='add-event'),
]