
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('members/',include('members.urls')),
    path('members/',include('django.contrib.auth.urls')),
]
