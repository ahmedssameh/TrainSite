from django.shortcuts import render
from .models import Train
# Create your views here.
def trains(request):
    return render(request, 'Train/train.html', {'tra': Train.objects.all()})


