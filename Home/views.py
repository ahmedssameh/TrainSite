from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'HomePage/Home.html', {})

def Info(request):
    return render(request,'user/Info.html',{})