from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.
x=[
    ('cairo', 'cairo'), ('Giza', 'Giza'), ('Alexandria', 'Alexandria'), ('Dakahlia', 'Dakahlia'),
    ('Sharkia', 'Sharkia'), ('Menoufia', 'Menoufia'), ('Qalyubia', 'Qalyubia'),
    ('Beheira', 'Beheira'), ('Gharbia', 'Gharbia'), ('Port Said', 'Port Said'),
    ('Damietta', 'Damietta'), ('Ismailia', 'Ismailia'), ('Suez', 'Suez'),
    (' Kafr El Sheikh', ' Kafr El Sheikh'), ('Fayoum', 'Fayoum'), ('Beni Suef', 'Beni Suef'),
    ('Matrouh', 'Matrouh'), ('El Alamein ', 'El Alamein '), ('North Sinai', 'North Sinai'),
    ('Minya', 'Minya'), ('Sinai', 'Sinai'), ('Minya', 'Minya'), ('Assiut', 'Assiut'),
    ('Sohag', 'Sohag'), ('Qena', 'Qena'), ('Luxor', 'Luxor'), ('Aswan', 'Aswan'), ('Red Sea', 'Red Sea'),
]
class Train(models.Model):
    model=models.CharField(max_length=50)
    dateTime=models.DateTimeField()
    source=models.CharField(max_length=50,choices=x)
    destination=models.CharField(max_length=50,choices=x)
    numberOfSeats=models.IntegerField()
    trainimg=models.ImageField(default='2.jpg')
    def __str__(self):
        return self.model
    def clean(self):
        if self.source==self.destination:
            raise ValidationError(_('Source and destination cannot be equal'))
