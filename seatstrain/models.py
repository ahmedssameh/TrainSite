from django.db import models
# Create your models here.
from django.db import models

# Create your models here.
train_stations = [
    ('cairo', 'cairo'), ('Giza', 'Giza'), ('Alexandria', 'Alexandria'), ('Dakahlia', 'Dakahlia'),
    ('Sharkia', 'Sharkia'), ('Menoufia', 'Menoufia'), ('Qalyubia', 'Qalyubia'),
    ('Beheira', 'Beheira'), ('Gharbia', 'Gharbia'), ('Port Said', 'Port Said'),
    ('Damietta', 'Damietta'), ('Ismailia', 'Ismailia'), ('Suez', 'Suez'),
    (' Kafr El Sheikh', ' Kafr El Sheikh'), ('Fayoum', 'Fayoum'), ('Beni Suef', 'Beni Suef'),
    ('Matrouh', 'Matrouh'), ('El Alamein ', 'El Alamein '), ('North Sinai', 'North Sinai'),
    ('Minya', 'Minya'), ('Sinai', 'Sinai'), ('Minya', 'Minya'), ('Assiut', 'Assiut'),
    ('Sohag', 'Sohag'), ('Qena', 'Qena'), ('Luxor', 'Luxor'), ('Aswan', 'Aswan'), ('Red Sea', 'Red Sea'),
]


class Seats(models.Model):
    train_number = models.PositiveIntegerField()
    train_car_number = models.PositiveIntegerField()
    trip_number = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=50, choices=train_stations)
    destination = models.CharField(max_length=50, choices=train_stations)
    NumberOfSeats = models.PositiveIntegerField(default=20)
    class Meta:
        ordering=['-NumberOfSeats']

    def sourcenotequaldestination(self):
        if self.source == self.destination:
            return 'Source and destination cannot be equal'
class SingleSeat(models.Model):
    train_number = models.PositiveIntegerField()
    train_car_number = models.PositiveIntegerField()
    trip_number = models.PositiveIntegerField()
    NumberSeat = models.IntegerField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    SS_date = models.DateField()
    SS_time = models.TimeField()
    SS_source = models.CharField(max_length=50, choices=train_stations)
    SS_destination = models.CharField(max_length=50, choices=train_stations)
    Booking = models.BooleanField(default=False)

    def sourcenotequaldestination(self):
        if self.SS_source== self.SS_destination:
            return 'Source and destination cannot be equal'


