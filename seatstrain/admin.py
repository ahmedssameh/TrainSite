from django.contrib import admin
# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Seats
from .models import SingleSeat
admin.site.register(Seats),
admin.site.register(SingleSeat),

