import random
from datetime import date, timedelta
from django.contrib.auth.models import User
from myapp.models import Venue, Event, MyclubUser

def run():
    # Clear old data
    Venue.objects.all().delete()
    Event.objects.all().delete()
    MyclubUser.objects.all().delete()
    User.objects.filter(username__startswith='testuser').delete()

    # 1️⃣ Create 10 Venues
    for i in range(1, 11):
        Venue.objects.create(
            name=f"Venue {i}",
            address=f"{i} Street, Area {i}",
            zip_code=f"6000{i}",
            phone=f"98765432{i}",
            website=f"https://venue{i}.com",
            email_address=f"venue{i}@test.com"
        )

    venues = list(Venue.objects.all())

    # 2️⃣ Create 10 Users + MyclubUsers
    for i in range(1, 11):
        user = User.objects.create_user(
            username=f"testuser{i}",
            password="pass1234",
            first_name=f"User{i}",
            last_name="Test"
        )
        MyclubUser.objects.create(
            user=user,
            phone=f"99999123{i}"
        )

    # 3️⃣ Create 10 Events
    for i in range(1, 11):
        Event.objects.create(
            title=f"Event {i}",
            event_date=date.today() + timedelta(days=i),
            venue=random.choice(venues),
            description=f"This is a description for event {i}."
        )

    print("✅ Dummy data inserted successfully!")
