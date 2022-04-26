from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Seats
from .models import SingleSeat
from .forms import UserUpdateForm
def seats(request):
    return render(request ,'SeatsTrain\Seats.html',{'seats': Seats.objects.all()})
def seat(request):
    SSSeat=SingleSeat.objects.all()
    context={'SSSeat': SSSeat}
    return render(request, 'SeatsTrain\Seat.html', context)
def Update(request,id):
   seat_id = SingleSeat.objects.get(id=id)
   if request.method =='POST':
      seat_save=UserUpdateForm(request.POST, request.FILES, instance=seat_id)
      if seat_save.is_valid():
           seat_save.save()
           messages.success(request, 'Your Book Is Done')
           return redirect('http://127.0.0.1:8000/')
   else:
       seat_save = UserUpdateForm(instance=seat_id)
   context = {'u_form': seat_save}
   return render(request,'seatsTrain/Update.html',context)


# Create your views here.
